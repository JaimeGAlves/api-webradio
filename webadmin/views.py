from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from core.models import PedidoMusica, Programacao, Equipe
from notices.models import Noticias, Imagem
from sponsors.models import Patrocinador
from analytics.models import ListenerStat
from .forms import NoticiaForm, PatrocinadorForm, ProgramacaoForm, EquipeForm
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max
from django.db.models.functions import TruncDate

@login_required(login_url='admin_login')
def dashboard(request):
    noticias_count = Noticias.objects.count()
    sponsors_count = Patrocinador.objects.count()
    pedidos_count = PedidoMusica.objects.count()
    
    # Pegar estatísticas atuais
    last_stat = ListenerStat.objects.first()
    current_listeners = last_stat.count if last_stat else 0
    
    return render(request, 'webadmin/dashboard.html', {
        'noticias_count': noticias_count,
        'sponsors_count': sponsors_count,
        'pedidos_count': pedidos_count,
        'current_listeners': current_listeners,
    })

@login_required(login_url='admin_login')
def listener_stats_api(request):
    # Retorna o total de ouvintes únicos por dia nos últimos 30 dias
    period = timezone.now() - timedelta(days=30)
    
    # Agrupar por dia e pegar o valor máximo de ouvintes únicos (total acumulado no dia)
    stats = ListenerStat.objects.filter(timestamp__gte=period) \
        .annotate(date=TruncDate('timestamp')) \
        .values('date') \
        .annotate(total_unique=Max('unique_count')) \
        .order_by('date')
    
    data = {
        'labels': [s['date'].strftime('%d/%m') for s in stats],
        'values': [s['total_unique'] for s in stats],
    }
    return JsonResponse(data)

@login_required(login_url='admin_login')
def noticias_list(request):
    noticias = Noticias.objects.all().order_by('-created_at')
    return render(request, 'webadmin/noticias_list.html', {
        'noticias': noticias
    })

@login_required(login_url='admin_login')
def noticia_form(request, pk=None):
    if pk:
        noticia = get_object_or_404(Noticias, pk=pk)
    else:
        noticia = None
        
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            noticia_obj = form.save(commit=False)
            if not pk:  # Nova notícia
                noticia_obj.created_by = request.user
            noticia_obj.updated_by = request.user
            noticia_obj.save()
            
            # Processar o upload múltiplo de imagens
            for f in request.FILES.getlist('imagens'):
                Imagem.objects.create(noticia=noticia_obj, imagem=f, rodape='Imagem anexada')
                
            messages.success(request, 'Notícia salva com sucesso!')
            return redirect('admin_noticias_list')
    else:
        form = NoticiaForm(instance=noticia)
        
    return render(request, 'webadmin/noticia_form.html', {
        'form': form,
        'is_edit': bool(pk)
    })

@login_required(login_url='admin_login')
@require_POST
def noticia_delete(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    noticia.delete()
    messages.success(request, 'Notícia excluída com sucesso!')
    return redirect('admin_noticias_list')

@login_required(login_url='admin_login')
@require_POST
def noticia_imagem_delete(request, img_id):
    img = get_object_or_404(Imagem, pk=img_id)
    noticia_id = img.noticia.pk
    img.delete()
    messages.success(request, 'Imagem removida com sucesso!')
    return redirect('admin_noticia_edit', pk=noticia_id)

@login_required(login_url='admin_login')
def patrocinadores_list(request):
    patrocinadores = Patrocinador.objects.all()
    return render(request, 'webadmin/patrocinadores_list.html', {
        'patrocinadores': patrocinadores
    })

@login_required(login_url='admin_login')
def patrocinador_form(request, pk=None):
    if pk:
        patrocinador = get_object_or_404(Patrocinador, pk=pk)
    else:
        patrocinador = None
        
    if request.method == 'POST':
        form = PatrocinadorForm(request.POST, request.FILES, instance=patrocinador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patrocinador salvo com sucesso!')
            return redirect('admin_sponsors_list')
    else:
        form = PatrocinadorForm(instance=patrocinador)
        
    return render(request, 'webadmin/patrocinador_form.html', {
        'form': form,
        'is_edit': bool(pk)
    })

@login_required(login_url='admin_login')
@require_POST
def patrocinador_delete(request, pk):
    patrocinador = get_object_or_404(Patrocinador, pk=pk)
    patrocinador.delete()
    messages.success(request, 'Patrocinador excluído com sucesso!')
    return redirect('admin_sponsors_list')

# Pedidos de Música
@login_required(login_url='admin_login')
def pedidos_list(request):
    pedidos = PedidoMusica.objects.all()
    return render(request, 'webadmin/pedidos_list.html', {'pedidos': pedidos})

@login_required(login_url='admin_login')
@require_POST
def pedido_marcar_lido(request, pk):
    pedido = get_object_or_404(PedidoMusica, pk=pk)
    pedido.lido = not pedido.lido
    pedido.save()
    status = "lido" if pedido.lido else "não lido"
    messages.success(request, f'Pedido marcado como {status}!')
    return redirect('admin_pedidos_list')

@login_required(login_url='admin_login')
@require_POST
def pedido_delete(request, pk):
    pedido = get_object_or_404(PedidoMusica, pk=pk)
    pedido.delete()
    messages.success(request, 'Pedido excluído com sucesso!')
    return redirect('admin_pedidos_list')

# Programacao
@login_required(login_url='admin_login')
def programacao_list(request):
    # Buscamos todos os programas e seus dias associados
    programas = Programacao.objects.all().prefetch_related('dias_semana').order_by('horario_inicio')
    
    # Criamos uma lista achatada para que o template consiga agrupar por dia corretamente
    # Um programa que passa em 3 dias aparecerá 3 vezes na lista (uma em cada seção de dia)
    programacao_flat = []
    for p in programas:
        for dia in p.dias_semana.all():
            programacao_flat.append({
                'dia_id': dia.id,
                'dia_nome': dia.nome,
                'detalhes': p
            })
    
    # Ordenamos a lista final por ID do dia (0-6) e depois por horário
    programacao_flat.sort(key=lambda x: (x['dia_id'], x['detalhes'].horario_inicio))
    
    return render(request, 'webadmin/programacao_list.html', {'programacao_flat': programacao_flat})

@login_required(login_url='admin_login')
def programacao_form(request, pk=None):
    if pk:
        programacao = get_object_or_404(Programacao, pk=pk)
    else:
        programacao = None
        
    if request.method == 'POST':
        form = ProgramacaoForm(request.POST, instance=programacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Programa salvo com sucesso!')
            return redirect('admin_programacao_list')
    else:
        form = ProgramacaoForm(instance=programacao)
        
    return render(request, 'webadmin/programacao_form.html', {
        'form': form,
        'is_edit': bool(pk)
    })

@login_required(login_url='admin_login')
@require_POST
def programacao_delete(request, pk):
    programacao = get_object_or_404(Programacao, pk=pk)
    programacao.delete()
    messages.success(request, 'Programa excluído com sucesso!')
    return redirect('admin_programacao_list')

# Equipe
@login_required(login_url='admin_login')
def equipe_list(request):
    equipe = Equipe.objects.all()
    return render(request, 'webadmin/equipe_list.html', {'equipe': equipe})

@login_required(login_url='admin_login')
def equipe_form(request, pk=None):
    if pk:
        equipe = get_object_or_404(Equipe, pk=pk)
    else:
        equipe = None
        
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membro da equipe salvo com sucesso!')
            return redirect('admin_equipe_list')
    else:
        form = EquipeForm(instance=equipe)
        
    return render(request, 'webadmin/equipe_form.html', {
        'form': form,
        'is_edit': bool(pk)
    })

@login_required(login_url='admin_login')
@require_POST
def equipe_delete(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    equipe.delete()
    messages.success(request, 'Membro da equipe excluído com sucesso!')
    return redirect('admin_equipe_list')

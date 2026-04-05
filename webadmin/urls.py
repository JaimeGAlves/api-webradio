from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='webadmin/login.html'), name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    
    # Noticias
    path('noticias/', views.noticias_list, name='admin_noticias_list'),
    path('noticias/novo/', views.noticia_form, name='admin_noticia_add'),
    path('noticias/<int:pk>/editar/', views.noticia_form, name='admin_noticia_edit'),
    path('noticias/<int:pk>/excluir/', views.noticia_delete, name='admin_noticia_delete'),
    path('noticias/imagem/<int:img_id>/excluir/', views.noticia_imagem_delete, name='admin_noticia_imagem_delete'),
    
    # Patrocinadores
    path('patrocinadores/', views.patrocinadores_list, name='admin_sponsors_list'),
    path('patrocinadores/novo/', views.patrocinador_form, name='admin_sponsor_add'),
    path('patrocinadores/<int:pk>/editar/', views.patrocinador_form, name='admin_sponsor_edit'),
    path('patrocinadores/<int:pk>/excluir/', views.patrocinador_delete, name='admin_sponsor_delete'),

    # Pedidos de Música
    path('pedidos/', views.pedidos_list, name='admin_pedidos_list'),
    path('pedidos/<int:pk>/lido/', views.pedido_marcar_lido, name='admin_pedido_marcar_lido'),
    path('pedidos/<int:pk>/excluir/', views.pedido_delete, name='admin_pedido_delete'),

    # Programação
    path('programacao/', views.programacao_list, name='admin_programacao_list'),
    path('programacao/novo/', views.programacao_form, name='admin_programacao_add'),
    path('programacao/<int:pk>/editar/', views.programacao_form, name='admin_programacao_edit'),
    path('programacao/<int:pk>/excluir/', views.programacao_delete, name='admin_programacao_delete'),

    # Equipe
    path('equipe/', views.equipe_list, name='admin_equipe_list'),
    path('equipe/novo/', views.equipe_form, name='admin_equipe_add'),
    path('equipe/<int:pk>/editar/', views.equipe_form, name='admin_equipe_edit'),
    path('equipe/<int:pk>/excluir/', views.equipe_delete, name='admin_equipe_delete'),
    
    # Analytics API
    path('api/stats/', views.listener_stats_api, name='admin_api_stats'),
]

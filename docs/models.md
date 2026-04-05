# Modelos de Dados

O projeto **API Webradio** possui duas aplicações principais com os seguintes modelos de dados:

## Aplicativo `notices` (Notícias)

### Noticias
Representa a notícia principal.
- `id` (PK, Automático)
- `titulo` (CharField, max_length=255, Único)
- `subtitulo` (TextField)
- `conteudo` (TextField)
- `created_at` (DateTimeField, auto_now_add)
- `updated_at` (DateTimeField, auto_now)
- `created_by` (ForeignKey -> User, null=True) - Usuário que cadastrou
- `updated_by` (ForeignKey -> User, null=True) - Último usuário que editou

### Fonte
As fontes ou referências de uma notícia.
- `id` (PK, Automático)
- `noticia` (ForeignKey -> Noticias, related_name='fontes')
- `nome` (CharField, max_length=255)
- `link` (URLField, max_length=255)

### Imagem
Galeria de imagens atrelada a uma notícia.
- `id` (PK, Automático)
- `noticia` (ForeignKey -> Noticias, related_name='imagens')
- `imagem` (ImageField, upload_to='noticias/')
- `rodape` (CharField, max_length=255)

---

## Aplicativo `sponsors` (Patrocinadores)

### Patrocinador
Armazena as informações dos patrocinadores e as mídias específicas para plataforma.
- `id` (PK, Automático)
- `nome` (CharField, max_length=255, Único)
- `link` (URLField, max_length=255)
- `imagem_app` (ImageField, upload_to='patrocinador_app/')
- `imagem_site` (ImageField, upload_to='patrocinador_site/')
- `created_at` (DateTimeField, auto_now_add)
- `updated_at` (DateTimeField, auto_now)

---

## Aplicativo `core` (Recursos da Rádio)

### PedidoMusica
Registro de pedidos feitos pelos ouvintes.
- `id` (PK)
- `nome_ouvinte` (CharField)
- `pedido` (CharField)
- `lido` (BooleanField) - Status de controle para o DJ
- `criado_em` (DateTimeField, auto_now_add)

### DiaSemana
Modelo de suporte para organizar os dias da semana de forma indexada.
- `id` (PK, Manually Assigned: 0-6) - Segue o padrão (0=Dom, 1=Seg...)
- `nome` (CharField, max_length=20) - Ex: "Segunda-feira"

### Programacao
Grade de horários da rádio, agora com suporte a múltiplos dias por entrada.
- `id` (PK)
- `dias_semana` (ManyToManyField -> DiaSemana) - Relacionamento flexível para programas que ocorrem em vários dias (ex: Seg-Sex).
- `horario_inicio` (TimeField)
- `horario_fim` (TimeField)
- `nome_programa` (CharField)
- `locutor` (ForeignKey -> Equipe, null=True) - Vínculo direto com a equipe

### Equipe
Membros da rádio.
- `id` (PK)
- `nome` (CharField)
- `descricao` (TextField)
- `foto` (ImageField, upload_to='equipe/')

---
Voltar para o [README](../README.md).

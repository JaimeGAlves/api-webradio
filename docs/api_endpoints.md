# Endpoints da API

Esta documentação lista todos os endpoints mapeados no arquivo de rotas. O prefixo base das rotas é `/api/`.

## Autenticação (JWT)
Os endpoints de autenticação recebem credenciais e retornam tokens JWT.

- `POST /api/token/`
  Gera um novo par de tokens (Access e Refresh) ao informar um usuário e senha válidos.
- `POST /api/token/refresh/`
  Gera um novo token de acesso usando um token de refresh válido.

- `GET /api/admin/`
  Abre o Django Admin clássico.

## Painel Administrativo Customizado (WebAdmin)
Interface visual moderna para gestão do conteúdo.
- `GET /painel/`
  Abre o Painel Administrativo (requer login).
- [Sub-rotas internas de gestão de Notícias, Patrocinadores, Equipe, Pedidos e Grade]

---

## Patrocinadores (`sponsors`)

Rotas responsáveis por gerenciar e expor os patrocinadores.

- `GET /api/teste/`
  Endpoint primário de teste do app.
- `POST /api/patrocinador/cadastrar/`
  Cadastra um novo patrocinador.
- `GET /api/patrocinador/`
  Lista patrocinadores gerais.
- `GET | PUT | DELETE /api/patrocinador/<int:pk>/`
  Consulta, atualiza ou deleta um patrocinador específico através de seu ID.
- `PUT | PATCH /api/patrocinador/editar/<int:pk>/`
  Modifica dados em um patrocinador específico (compatível com views de edição).
- `GET /api/patrocinador/app/`
  Obtém os dados/imagens dos patrocinadores com foco no aplicativo móvel.
- `GET /api/patrocinador/site/`
  Obtém os dados/imagens dos patrocinadores com foco no uso pelo site.

---

## Notícias (`notices`)

Rotas para listar e administrar as notícias publicadas pela rádio, bem como suas fontes e imagens.

- `POST /api/noticias/cadastrar/`
  Cadastra uma nova notícia (com suas propriedades, arquivos e fontes anexadas).
- `GET /api/noticias/`
  Traz a listagem de notícias disponíveis.
- `GET | PUT | DELETE /api/noticias/<int:pk>/`
  Usado para buscar os detalhes, modificar todo o bloco de informações ou deletar uma notícia preexistente.
- `PUT | PATCH /api/noticias/editar/<int:pk>/`
  Endpoint auxiliar para editar ou atualizar dados parciais da notícia pelo seu ID.

---

## Recursos Gerais (`core`)

Endpoints que alimentam as interações e informações institucionais no App.

- `POST /api/pedidos/`
  **[PÚBLICO]** Permite que qualquer ouvinte envie um pedido de música.
- `GET /api/programacao/`
  Retorna a grade completa de horários de todos os programas.
- `GET /api/equipe/`
  Retorna a lista de membros da rádio (Fotos e biografias).

---
Voltar para o [README](../README.md).

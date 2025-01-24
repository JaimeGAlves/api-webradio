from django.urls import path

from notices.views import (
    NoticiasCreateView, 
    NoticiasDetalhesView,
)

urlpatterns = [
    path('noticias/cadastrar/', NoticiasCreateView.as_view()),
    path('noticias/', NoticiasDetalhesView.as_view()),
    path('noticias/<int:pk>/', NoticiasDetalhesView.as_view()),
    path('noticias/editar/<int:pk>/', NoticiasDetalhesView.as_view()),
]

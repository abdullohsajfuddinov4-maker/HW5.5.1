from django.urls import path,include
from .views import d_nomi,m_nomi

urlpatterns = [
    path('d_nomi/',d_nomi),
    path('m_nomi/',m_nomi),
]
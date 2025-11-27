from django.urls import path,include
from .views import ustoz_nomi,qaruvchi_gurih

urlpatterns = [
    path('ustoz_nomi/',ustoz_nomi),
    path('qaruvchi_gurih/',qaruvchi_gurih)

]
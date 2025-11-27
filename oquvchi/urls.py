from .views import oquvchilar_nomi,group
from django.urls import path,include
urlpatterns = [
    path('oquvchi/',oquvchilar_nomi),
    path('group/',group)
]
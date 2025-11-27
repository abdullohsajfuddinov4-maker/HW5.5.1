from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def oquvchilar_nomi(request):
    return HttpResponse('ali,vali,umar,begi')
def group(requset):
    return HttpResponse('10B')


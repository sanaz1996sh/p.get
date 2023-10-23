from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def contact(request):
    n=request.GET.get("name")
    e=request.GET.get("email")
    m=request.GET.get("message")
    if(n and e and m):
        contactcls.objects.create(name=n,email=e,message=m)
        return render(request,"getapp/message.html")

    return render(request,"getapp/contact.html")

from django.shortcuts import render
from .models import  Regist 
from django.contrib import messages 

# Create your views here.



def views_form(request):

    if request.method == "POST":

        name = request.POST.get('first')
        pre_name = request.POST.get('last')
        phone = request.POST.get('telp')
        adress = request.POST.get('mail')
        why = request.POST.get('desc')

        if name and pre_name and phone and adress and why:
            Regist.objects.create( first_name= name,
                                  last_name=pre_name,
                                  tel = phone,
                                  email= adress,
                                  body=why)

            messages.success(request, "Merci d'avoir rerserver votre place!!!")

    return render(request, 'index.html', {} )
from django.shortcuts import render,redirect
from . models import *
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def form_data(request):
    if request.method  == 'POST':
      name= request.POST['name']
      email=request.POST['email']
      phone=request.POST['phone']
      password=make_password(request.POST['password'])
      if Register.objects.filter(email=email).exists():
        messages.error(request,"email already exists")
        
      elif Register.objects.filter(phone=phone).exists():
            messages.error(request,"contact already exists")
      else:
            Register.objects.create(name=name,email=email,phone=phone,password=password) 
            return render(request,'login.html')

    else:
         return render(request,'index.html')



        
def login_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Register.objects.filter(email=email).exists():
             obj =Register.objects.get(email=email)
             password =obj.password
             if check_password(password,password):
                return redirect('login')
                # return render(request,'welcome.html')
             else:
                data = Register.objects.all()
                return render(request,"table.html",{"data":data})
        else:
             return HttpResponse('email is not registered')
             return render(request,'table.html')


        
def delete(request):
    
   uid=request.GET['uid']
   Register.objects.get(id=uid).delete()
   data=Register.objects.all()
   return render(request,'table.html',{'data':data})


#USE UPDATE DATA

def update(request,uid):
    data = Register.objects.get(id=uid)
    return render(request,'update.html',{'data':data})


def table(request):
     data=Register.objects.all()
     return render(request,'table.html',{'data':data})



def form_update(request):  

    if request.method == "POST":
        uid = request.POST['uid']
        name =request.POST['name']
        email =request.POST['email']
        phone=request.POST['phone']
        password =request.POST['password']
        Register.objects.filter(id=uid).update(name=name,email=email,phone=phone,password=password)
        return redirect('/table/')
    else:
        return render(request,'update.html')




    
        



from django.shortcuts import render
from .models import Register

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        obj = Register(name=name,email=email,date=date,time=time)
        obj.save()
    return render(request,'register.html')

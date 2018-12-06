from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from fashion.models import User


def index(request):
    tel = request.COOKIES.get('tel')
    return render(request, 'index.html', context={'tel': tel})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        tel = request.POST.get('tel')
        password = request.POST.get('password')

        users = User.objects.filter(tel=tel).filter(password=password)
        if users.count():
            response = redirect('fashion:index')
            response.set_cookie('tel', tel)
            return response

        else:
            return render(request,'login.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'register01.html')
    elif request.method == 'POST':
        tel = request.POST.get('tel')

        password = request.POST.get('password')


        user = User()
        user.tel = tel
        user.password = password
        user.save()

        response = redirect('fashion:index')

        response.set_cookie('tel',tel)

        #return HttpResponse('稍等')
        return response


def exit(request):
    response = redirect('fashion:index')
    response.delete_cookie('tel')
    return response



def car(request):
    return render(request, 'car.html')


def goods(request):
    return render(request, 'goods.html')


def list(request):
    return render(request, 'list.html')



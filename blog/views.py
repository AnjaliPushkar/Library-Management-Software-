from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import create

def home2(request):
    blog = create.objects
    return render(request, 'blog/home2.html', {'blog':blog})


def add(request):
    if request.method == 'POST':
        if request.POST['code'] and request.POST['title'] and request.POST['bookno'] and request.POST['body'] and request.POST['no']  and request.FILES['icon'] and request.FILES['image'] :
            if request.POST['code']  == 'L':
                prod = create()
                prod.title = request.POST['title']
                prod.bookno = request.POST['bookno']
                prod.body = request.POST['body']
                prod.no = request.POST['no']
                prod.icon = request.FILES['icon']
                prod.image = request.FILES['image']
                prod.pub_date = timezone.datetime.now()
                prod.hunter = request.user
                prod.save()
                return redirect('/blog/' + str(prod.id))
            else:
                return render(request, 'blog/add.html', {'error' : 'code is incorrect'})
        else:
            return render(request, 'blog/add.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'blog/add.html')

def detail(request, prod_id):
    prod = get_object_or_404(create, pk=prod_id)
    return render(request, 'blog/detail.html', {'prod':prod})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import issuebook, returnbook
from django.utils import timezone

def issue(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['clgid'] and request.POST['bookname'] and request.POST['bookid'] and request.POST['code']:
            if request.POST['code']  == 'I':
                prod = issuebook()
                prod.username = request.POST['username']
                prod.clgid = request.POST['clgid']
                prod.bookname = request.POST['bookname']
                prod.bookid = request.POST['bookid']
                prod.pub_date = timezone.datetime.now()
                prod.save()
                return render(request, 'clg/book.html')
            else:
                return render(request, 'blog/issue.html', {'error' : 'code is incorrect'})
        else:
            return render(request, 'books/issue.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'books/issue.html')

def ret(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['clgid'] and request.POST['bookname'] and request.POST['bookid'] and request.POST['code']:
            if request.POST['code']  == 'R':
                pro = returnbook()
                pro.username = request.POST['username']
                pro.clgid = request.POST['clgid']
                pro.bookname = request.POST['bookname']
                pro.bookid = request.POST['bookid']
                pro.pub_date = timezone.datetime.now()
                pro.save()
                return render(request, 'clg/book.html')
            else:
                return render(request, 'blog/return.html', {'error' : 'code is incorrect'})
        else:
            return render(request, 'books/return.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'books/return.html')

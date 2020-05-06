from django.contrib import admin
from django.urls import path, include
from .import views
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issue/', views.issue, name='issue'),
    path('ret/', views.ret, name='ret'),

]

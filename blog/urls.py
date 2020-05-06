from django.contrib import admin
from django.urls import path, include
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add, name='add'),
    path('<int:prod_id>', views.detail, name='detail'),
    path('home2/', views.home2, name='home2'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

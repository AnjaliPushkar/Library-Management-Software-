from django.contrib import admin

# Register your models here.


from .models import returnbook

admin.site.register(returnbook)

from .models import issuebook

admin.site.register(issuebook)

from django.contrib import admin

# Register your models here.
from .models import User, Customerinfo

admin.site.register(User)
admin.site.register(Customerinfo)
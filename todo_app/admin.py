from django.contrib import admin
from .models import Tasks, CompletedTask

# Register your models here.
admin.site.register(Tasks)
admin.site.register(CompletedTask)
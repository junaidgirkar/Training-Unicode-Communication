from django.contrib import admin
from .models import Quiz,Question,Answer,Result
# Register your models here.

admin.site.site_header = 'My administration'
admin.site.site_title = 'Classroom'
admin.site.index_title = 'Site admin panel'

admin.site.register((Quiz,Question,Answer,Result))
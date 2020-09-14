from django.contrib import admin
from mcqQuiz.models import *
# Register your models here.

admin.site.site_title = 'Quiz'
admin.site.site_header = 'UNICODE QUIZ APP'

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
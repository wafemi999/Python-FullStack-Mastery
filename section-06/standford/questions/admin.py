from django.contrib import admin
from questions.models.exam_choice import ExamChoice
from questions.models.exam_question import ExamQuestion

# Register your models here.
admin.site.register(ExamChoice)
admin.site.register(ExamQuestion)
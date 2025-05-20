from django.urls import path
from questions.views.exam_choice_view import *

app_name = 'questions'
urlpatterns = [
    path('choices/all', ExamChoiceListCreateView.as_view(), name='exam-choice-list'),
    path('choices/<int:pk>', ExamChoiceDetailUpdateDeleteView.as_view(), name='exam-choice-detail')
]
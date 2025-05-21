from django.urls import path
from questions.views.exam_choice_view import *
from questions.views.exam_question_view import *

app_name = 'questions'
urlpatterns = [
    # exam questions patterns
    path('all', ExamQuestionListCreateView.as_view(), name='exam-questions-list'),
    path('<int:pk>', ExamQuestionDetailUpdateDeleteView.as_view(), name='exam-questions-detail'),

    # exam questions-choices patterns
    path('choices/all', ExamChoiceListCreateView.as_view(), name='exam-choices-list'),
    path('choices/<int:pk>', ExamChoiceDetailUpdateDeleteView.as_view(), name='exam-choice-detail')
]
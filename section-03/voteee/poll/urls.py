from django.urls import path
from poll.views import *

app_name = 'poll'
urlpatterns = [
    path('list', index, name='list-view'),
    path('<int:question_id>/', detail, name='question-detail'),
    path('<int:question_id>/results', results, name='poll-results'),
    path('<int:question_id>/vote', vote, name='poll-vote')
]
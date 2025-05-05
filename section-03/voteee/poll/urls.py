from django.urls import path
from poll.views import *

app_name = 'poll'
urlpatterns = [
    path('list', IndexView.as_view(), name='list-view'),
    path('<int:pk>/', QDetailView.as_view(), name='question-detail'),
    path('<int:pk>/results', ResultsView.as_view(), name='poll-results'),
    path('<int:question_id>/vote', vote, name='poll-vote')
]
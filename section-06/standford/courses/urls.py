from django.urls import path
from courses.views.course_views import *
from courses.views.exam_views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', CoursesViewSet)


app_name = 'courses'
urlpatterns = [
    # courses patterns
    # path('all', CoursesViewSet.as_view({'get': 'list'}), name='course-list'),
    # path('<int:pk>', CoursesViewSet.as_view({'get' : 'retrieve'}), name='course-detail'),

    #  single route that perfomrms/handles all request -> get, retrieve, list, put, delete
    # exams patterns
    path('exam/all', ExamListCreateView.as_view(), name='exam-list'),
    path('exam/<slug:pk>', ExamDetailUpdateDeleteView.as_view(), name='exam-detail')
] + router.urls


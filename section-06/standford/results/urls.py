from rest_framework.routers import SimpleRouter
from results.views.exam_attempt_view import ExamAttemptViewSet
from results.views.student_answer import StudentAnswerViewSet
from results.views.result_view import ResultViewSet
from django.urls import path, include


router = SimpleRouter()
router.register('exam-attempt', ExamAttemptViewSet)
router.register('student-ansswer', StudentAnswerViewSet)
router.register('', ResultViewSet)

urlpatterns = [
    path('', include(router.urls))
]

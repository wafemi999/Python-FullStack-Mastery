from django.urls import path
from rest_framework.routers import SimpleRouter
from accounts.views.admin_view import AdminsViewSet
from accounts.views.student_view import StudentsViewSet
from accounts.views.signup_view import SignUpView
from accounts.views.auth_view import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from accounts.views.login_view

router = SimpleRouter()
router.register(r'students', StudentsViewSet)
router.register(r'admin', AdminsViewSet)

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    # path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls


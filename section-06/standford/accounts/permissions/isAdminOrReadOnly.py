from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    message = 'Only admin can modify data'

    def has_permission(self, request, view):
        # get request scenario
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrStudentOnly(BasePermission):
    message = 'Only student or superusers can view this route'
    def has_permission(self, request, view):
        if request.user.is_student or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
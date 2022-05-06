from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAdm(BasePermission):
    def has_permission(self, request:Request):
        
        if request.user.is_admin:
            return True
        return False
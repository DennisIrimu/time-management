from rest_framework.permissions import BasePermission
from .models import Projects

class Manager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Projects):
            return obj.owner == request.user
        return obj.owner == request.user
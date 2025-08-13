# tasks/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """
    Allow read for authenticated users on list;
    but detail read/update/delete only if owner.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

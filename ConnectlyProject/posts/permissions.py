from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrModerator(BasePermission):
    """
    Allows access only to users with Admin or Moderator roles.
    Assumes that the User model has a "role" field and that the role instance has a "name" attribute.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.role is None:
            return False
        return user.role.name in ['Admin', 'Moderator']

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an attribute "author".
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request.
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Otherwise, the user must be the owner.
        return obj.author == request.user
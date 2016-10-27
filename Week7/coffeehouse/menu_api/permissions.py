from rest_framework import permissions


class IsCreatedByOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print("in permission check")
        # allow anyone for a get request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

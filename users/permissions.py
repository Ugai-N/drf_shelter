from rest_framework.permissions import BasePermission


class IsDogOwner(BasePermission):
    message = "Вы не являетесь автором"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsPublicDog(BasePermission):
    message = "Собака не опубликована"

    def has_object_permission(self, request, view, obj):
        return obj.is_public


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.role == 'moderator':
            return True
        return False

from rest_framework import permissions
 


class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
      
        if request.method == 'GET':
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
      
        if request.method == 'GET':
            return True
        return obj.user.id == request.user.id
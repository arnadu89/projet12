from rest_framework import permissions
from crm.models import User


class IsUserSalesTeam(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False

        if request.user.team is User.Team.SALES:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user is obj.sales_contact:
            return True

        return False

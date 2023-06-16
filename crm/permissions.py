from datetime import datetime

from rest_framework import permissions
from crm.models import User


class IsUserSalesTeamToCreateUpdateDelete(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False

        allowed_methods = ["GET", "POST", "PATCH", "PUT", "DELETE"]
        if request.user.team == User.Team.SALES and request.method in allowed_methods:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        client_event = obj.client
        if client_event in request.user.get_clients():
            return True

        return False


class IsClientSalesContact(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return True

        return False


class IsContractClientSalesContact(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.client.sales_contact:
            return True

        return False


class IsClientSupportReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return False

        is_user_support_of_client_events = obj.event_set.filter(
            support_contact=request.user
        ).exists()
        if is_user_support_of_client_events:
            return True

        return False


class IsSupportAndEventIsNotFinishToReadUpdate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False

        if request.user.team == User.Team.SUPPORT and request.method in ["GET", "PATCH"]:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.event_date < datetime.now(obj.event_date.tzinfo):
            return False

        return True

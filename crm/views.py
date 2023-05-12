from django.shortcuts import render
from rest_framework import viewsets
from crm.models import *
from crm.serializers import *
from crm.permissions import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (permissions.IsAdminUser | IsUserSalesTeam,)
    permission_classes = (permissions.IsAdminUser | permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.team is User.Team.SALES:
            queryset = Client.objects.all()
        elif user.team == User.Team.SUPPORT:
            print("support team")
            queryset = Client.objects.filter(
                event__support_contact=user
            )
        else:
            queryset = Client.objects.all()

        return queryset


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

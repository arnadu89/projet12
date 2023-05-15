from django.shortcuts import render
from rest_framework import viewsets
from crm.models import *
from crm.serializers import *
from crm.permissions import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (
        permissions.IsAdminUser | IsClientSalesContact | IsClientSupportReadOnly,
    )

    def get_queryset(self):
        user = self.request.user
        if user.team == User.Team.SALES:
            queryset = Client.objects.filter(
                sales_contact=user
            )
        elif user.team == User.Team.SUPPORT:
            queryset = Client.objects.filter(
                event__support_contact=user
            )
        else:
            queryset = Client.objects.all()

        return queryset


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = (
        permissions.IsAdminUser | IsContractClientSalesContact,
    )

    def get_queryset(self):
        user = self.request.user
        if user.team == User.Team.SALES:
            queryset = Contract.objects.filter(
                sales_contact=user
            )
        else:
            queryset = Contract.objects.all()

        return queryset


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAdminUser | IsSupportAndEventIsNotFinishToUpdate
        | IsUserSalesTeamToCreate,)

    def get_queryset(self):
        user = self.request.user
        if user.team == User.Team.SALES:
            queryset = Event.objects.filter(
                client__sales_contact=user
            )
        elif user.team == User.Team.SUPPORT:
            queryset = Event.objects.filter(
                support_contact=user
            )
        else:
            queryset = Event.objects.all()

        return queryset

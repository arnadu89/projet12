import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from crm.models import *
from crm.serializers import *
from crm.permissions import *
from django_filters import rest_framework as filters


class ClientFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Client
        fields = ["last_name", "email"]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    serializer_class = ClientSerializer
    create_serializer_class = ClientCreateSerializer

    permission_classes = [
        permissions.IsAdminUser | IsClientSalesContact | IsClientSupportReadOnly
    ]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def get_queryset(self):
        return self.request.user.get_clients()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ContractFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name="client__last_name", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="client__email", lookup_expr="icontains")
    date_created = django_filters.NumberFilter()
    amount = django_filters.NumberFilter()

    class Meta:
        model = Contract
        fields = ["last_name", "email", "date_created", "amount"]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    create_serializer_class = ContractCreateSerializer
    permission_classes = (
        permissions.IsAdminUser | IsContractClientSalesContact,
    )

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContractFilter

    def get_queryset(self):
        return self.request.user.get_contracts()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["sales_contact"] = self.request.user
        return context

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class EventFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name="client__last_name", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="client__email", lookup_expr="icontains")
    event_date = django_filters.NumberFilter()

    class Meta:
        model = Event
        fields = ["last_name", "email", "event_date"]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    create_serializer_class = EventCreateSerializer
    permission_classes = (
        permissions.IsAdminUser | IsSupportAndEventIsNotFinishToUpdate
        | IsUserSalesTeamToCreate,)

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_queryset(self):
        return self.request.user.get_events()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["sales_contact"] = self.request.user
        return context

from rest_framework import serializers
from crm.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
        )


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

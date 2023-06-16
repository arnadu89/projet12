from rest_framework import serializers
from crm.models import *


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'team']


class ClientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'complete_name']


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = UserSimpleSerializer()

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
    sales_contact = UserSimpleSerializer()
    client = ClientSimpleSerializer()

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

    def validate(self, data):
        if not self.context["sales_contact"].get_clients().filter(id=data["client"].id).exists():
            raise serializers.ValidationError({
                "client": "You are not the sales contact of this client for creating contract.",
            })

        return data


class EventSerializer(serializers.ModelSerializer):
    client = ClientSimpleSerializer()
    support_contact = UserSimpleSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        if not self.context["sales_contact"].get_clients().filter(id=data["client"].id).exists():
            raise serializers.ValidationError({
                "client": "You are not the sales contact of this client for creating event.",
            })

        return data


class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'support_contact',
            'event_status',
            'attendees',
            'event_date',
            'notes',
        )

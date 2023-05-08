from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from crm.models import *


class UserAdmin(DjangoUserAdmin):
    fieldsets = [
        "username", "first_name", "last_name", "email_address",
        "active", "staff_status"
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["complete_name", "company_name", "sales_contact"]


class ContractAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "contract_admin_list_display",
        "date_created",
        "sales_contact",
    ]

    def contract_admin_list_display(self, obj):
        return f"{obj.client} from {obj.client.company_name}"


admin.site.register(User, DjangoUserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)

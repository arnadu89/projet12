from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from crm.models import *
from django.utils.translation import gettext_lazy as _


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "team",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "team",
                ),
            },
        ),
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "complete_name",
        "company_name",
        "sales_contact",
    ]


class ContractAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "contract_admin_list_display",
        "date_created",
        "sales_contact",
    ]

    def contract_admin_list_display(self, obj):
        return f"{obj.client} from {obj.client.company_name}"


class EventAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "event_date",
        "event_status",
        "support_contact",
    ]


class EventStatusAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventStatus, EventStatusAdmin)

import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import User


class UserAdminExportCSVMixin:

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin, UserAdminExportCSVMixin):
    actions = ["export_as_csv"]

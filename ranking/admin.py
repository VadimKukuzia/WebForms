import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import *


class RankingAdminExportCSVMixin:

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


@admin.register(EconomicFire)
class EconomicFireAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(EconomicBlastFireBall)
class EconomicBlastFireBallAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(EconomicBlastShockWave)
class EconomicBlastShockWaveAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(SocialFire)
class SocialFireAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(SocialBlastFireBall)
class SocialBlastFireBallAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(SocialBlastShockWave)
class SocialBlastShockWaveAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(EnvironmentalFire)
class EnvironmentalFireAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(EnvironmentalBlastFireBall)
class EnvironmentalBlastFireBallAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]


@admin.register(EnvironmentalBlastShockWave)
class EnvironmentalBlastShockWaveAdmin(admin.ModelAdmin, RankingAdminExportCSVMixin):
    actions = ["export_as_csv"]

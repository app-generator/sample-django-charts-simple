# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin

from app.models import Sale
from app.models import Stats

class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale
        fields = ['id', 'amount', 'product_name', 'created_time']


@admin.register(Sale)
class SaleAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'amount', 'created_time']
    search_fields = ['product_name']
    resource_class = SaleResource

class StatsResource(resources.ModelResource):
    class Meta:
        model = Stats
        fields = ['year', 'prod1_sales', 'prod2_sales', 'prod3_sales']

@admin.register(Stats)
class StatsAdmin(ImportMixin, admin.ModelAdmin):
    list_display  = ['year', 'prod1_sales', 'prod2_sales', 'prod3_sales']
    search_fields = ['year']
    resource_class = StatsResource

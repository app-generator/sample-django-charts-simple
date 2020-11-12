# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _
from django.db.models.functions import TruncYear


class Sale(models.Model):
    amount = models.FloatField(_('amount'), db_index=True)
    product_name = models.CharField(_('product name'), max_length=40, db_index=True)
    created_time = models.DateTimeField(verbose_name=_('creation On'), db_index=True)
    updated_time = models.DateTimeField(verbose_name=_('modified On'), auto_now=True)

    class Meta:
        verbose_name = _('sale')
        verbose_name_plural = _('sales')

    @classmethod
    def get_sales_report(cls):
        annotates = {'total_amount': Sum('amount')}

        sales = cls.objects.annotate(
            year=TruncYear('created_time')
        ).values('product_name', 'year').order_by().annotate(**annotates)

        data = {}
        for sale in sales:
            if sale['year'].year not in data:
                data[sale['year'].year] = {}

            data[sale['year'].year][sale['product_name']] = sale['total_amount']

        labels = list(sales.values_list('product_name', flat=True).distinct())
        return data, labels

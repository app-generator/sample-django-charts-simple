# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from app.models import Sale


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')

    data, labels = Sale.get_sales_report()

    context['chart_data'] = json.dumps({
        'element': 'morris-bar-chart',
        'data': data,
        'xkey': 'y',
        'barSizeRatio': 0.70,
        'barGap': 3,
        'resize': True,
        'responsive': True,
        'ykeys': ['a', 'b', 'c'],  # it can be custom
        'labels': labels,
        'barColors': ['0-#1de9b6-#1dc4e9', '0-#899FD4-#A389D4', '#04a9f5']  # it can be custom
    })

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

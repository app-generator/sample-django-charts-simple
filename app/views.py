# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from app.models import Sale, Stats

def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')

    # -----------------------------------------------
    # Extract data from Sale tables
    # -----------------------------------------------

    # sales, labels = Sale.get_sales_report()
    # data = [
    #     {
    #         'y': year,
    #         'a': '{:.2f}'.format(sales[year].get('A')),
    #         'b': '{:.2f}'.format(sales[year].get('B')),
    #         'c': '{:.2f}'.format(sales[year].get('C'))
    #     } for year in sales
    # ]

    # -----------------------------------------------
    # Use data from stats
    # -----------------------------------------------

    # stats, labels = Stats.get_report()
    # data = [
    #     {
    #         'y': year,
    #         'a': '{:.2f}'.format( stats[year].get('prod1_sales') ), # 'a': '{:.2f}'.format( 30  ),
    #         'b': '{:.2f}'.format( stats[year].get('prod2_sales') ), # 'b': '{:.2f}'.format( 180 ),
    #         'c': '{:.2f}'.format( stats[year].get('prod3_sales') )  # 'c': '{:.2f}'.format( 80  )
    #     } for year in stats
    # ]

    # context['chart_data'] = json.dumps({
    #     'element': 'morris-bar-chart',
    #     'data': data,
    #     'xkey': 'y',
    #     'barSizeRatio': 0.70,
    #     'barGap': 3,
    #     'resize': True,
    #     'responsive': True,
    #     'ykeys': ['a', 'b', 'c'],  # it can be custom
    #     'labels': labels,
    #     'barColors': ['0-#1de9b6-#1dc4e9', '0-#899FD4-#A389D4', '#04a9f5']  # it can be custom
    # })

    # ------------------------------------------------
    # Load from File -> +sample_data/chart_morris.json
    # ------------------------------------------------

    with open('sample_data/chart_morris.json', 'r') as f:
        context['chart_data'] = json.dumps(json.load(f))

    return HttpResponse(html_template.render(context, request))

def charts_file(request):
    context = {'segment': 'charts_from_file'}
    html_template = loader.get_template('charts-from-file.html')

    with open('sample_data/chart_morris.json', 'r') as f:
        context['chart_data'] = json.dumps(json.load(f))

    return HttpResponse(html_template.render(context, request))    

def charts_input(request):
    context = {'segment': 'charts_from_input'}
    html_template = loader.get_template('charts-from-input.html')

    # -----------------------------------------------
    # Use data from STATS Table
    # -----------------------------------------------

    stats, labels = Stats.get_report()
    data = [
        {
            'y': year,
            'a': '{:.2f}'.format( stats[year].get('prod1_sales') ), 
            'b': '{:.2f}'.format( stats[year].get('prod2_sales') ), 
            'c': '{:.2f}'.format( stats[year].get('prod3_sales') )  
        } for year in stats
    ]

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

def charts_load(request):
    context = {'segment': 'charts_from_load'}
    html_template = loader.get_template('charts-from-load.html')

    # -----------------------------------------------
    # Extract data from Sale table 
    # -----------------------------------------------

    sales, labels = Sale.get_sales_report()
    data = [
        {
            'y': year,
            'a': '{:.2f}'.format(sales[year].get('A')),
            'b': '{:.2f}'.format(sales[year].get('B')),
            'c': '{:.2f}'.format(sales[year].get('C'))
        } for year in sales
    ]

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

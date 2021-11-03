from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    filter_param = request.GET.get('sort')
    phones_list = Phone.objects.all()
    if filter_param:
        phones_list = phones_list.order_by(filter_param)
    context = {
        'phones_list': phones_list,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

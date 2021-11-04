from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    filter_param = request.GET.get('sort')
    order_param = request.GET.get('order')
    phones_list = Phone.objects.all()
    if filter_param:
        phones_list = phones_list.order_by(filter_param)
    if order_param:
        phones_list = phones_list.desc(order_param)

    context = {
        'phones_list': phones_list,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)

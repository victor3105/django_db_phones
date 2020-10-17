from django.urls import reverse
from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    # Default behavior is to show phone in the order
    # in which they are stored in the database
    phones = Phone.objects.all()
    # Sort phones
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    phone_list = []
    for phone in phones:
        phone_info = {'Name': phone.name, 'Price': phone.price,
                      'Image': phone.image, 'URL': f'{reverse("catalog")}{phone.slug}'}
        phone_list.append(phone_info)
    # For sorting
    catalog_url = reverse('catalog').rstrip('/')
    context = {'phones': phone_list, 'catalog_url': catalog_url}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).get()
    phone_info = {'Name': phone.name, 'Price': phone.price,
                  'Image': phone.image, 'Date': phone.release_date,
                  'LTE': phone.lte_exists}
    context = {'phone': phone_info}
    return render(request, template, context)

from django.shortcuts import render
from django.views import generic

from apps.categories.models import Category
from apps.products.models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'base/../../templates/index.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['left_categories'] = Category.objects.filter(parent=None)
        context['dumbbells_product'] = Product.objects.filter(category__title='Гантели')[:5]
        context['protein_product'] = Product.objects.filter(category__title='Протойн')[:5]
        context['sportswear_product'] = Product.objects.filter(category__title='Спортивная одежда')[:5]

        return context
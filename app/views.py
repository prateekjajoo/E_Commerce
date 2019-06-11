from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product
# Create your views here.


class HomePageView(TemplateView):

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.order_by('?')
        category_data = Product.objects.values_list('category', 'company_name').distinct()
        category_dict = {}

        for category in category_data:
            if category[0] in category_dict:
                temp = category_dict[category[0]]
                temp.append(category[1])
                category_dict[category[0]] = temp
            else:
                category_dict[category[0]] = [category[1]]

        request.session['category_dict'] = category_dict
        return render(request, 'shopper/index.html', {'object_list': object_list, 'category_dict': category_dict})


class ProductView(TemplateView):

    def get(self, request, *args, **kwargs):
        category = self.kwargs['category_name']
        object_list = Product.objects.filter(category=category)
        if self.kwargs.get('subcategory_name'):
            object_list = Product.objects.filter(category=category, company_name=self.kwargs['subcategory_name'])
        return render(request, 'shopper/products.html', {'object_list': object_list})


class ProductDetailsView(TemplateView):
    # template_name = 'shopper/product_detail.html'
    def get(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        obj = Product.objects.get(id=self.kwargs['pk'])
        related_obj = Product.objects.filter(category=obj.category).order_by('?')
        return render(request, 'shopper/product_detail.html', {'data': obj, 'related_obj': related_obj})


class CartView(TemplateView):
    template_name = 'shopper/cart.html'


class CheckOutView(TemplateView):
    template_name = 'shopper/checkout.html'


class RegisterView(TemplateView):
    template_name = 'shopper/register.html'


class ContactView(TemplateView):
    template_name = 'shopper/contact.html'

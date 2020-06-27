from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView,ListView

# App Imports
from .forms import AddProductForm
from .models import ProductCategory, Product


# Create your views here.

class HomepageView(TemplateView):
    http_method_names = ['get']
    template_name = "index.html"


class AddProductView(CreateView):
    http_method_names = ['get', 'post']
    template_name = 'AddProduct.html'

    def get(self, request, **kwargs):
        form = AddProductForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        new_product = AddProductForm(request.POST)

        if new_product.is_valid():
            new_product.save()
            context = {
                'message': 'Product Saved successfully!',
                'danger': False,
            }
            return render(request,'index.html',context)
        else:
            context = {
                'message': 'Failed To Save The Product!',
                'danger': True,
            }
            return render(request, self.template_name,context)


class ListProductView(ListView):
    http_method_names = ['get','post']
    template_name = 'ListProduct.html'

    def get(self, request, *args, **kwargs):
        prod_objects = Product.objects.all()
        context = {
            'list': prod_objects
        }
        return render(request, self.template_name, context)



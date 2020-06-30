from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView

# App Imports
from .forms import AddProductForm
from .models import ProductCategory,Product


# Create your views here.

class HomepageView(TemplateView) :
    http_method_names = ['get']
    template_name = "index.html"


class AddProductView(CreateView) :
    http_method_names = ['get','post']
    template_name = 'AddProduct.html'

    def get(self,request,**kwargs) :
        form = AddProductForm()
        context = {
            'form' : form
        }
        return render(request,self.template_name,context)

    def post(self,request,**kwargs) :

        new_product = AddProductForm(request.POST, request.FILES)

        if new_product.is_valid() :
            new_product.save()
            context = {
                'message' : 'Product Saved successfully!',
                'danger' : False,
            }
            return render(request,'index.html',context)
        else :
            context = {
                'message' : 'Failed To Save The Product!',
                'danger' : True,
                'form' : new_product,
            }
            return render(request,self.template_name,context)


class ListProductView(ListView) :
    http_method_names = ['get','post']
    template_name = 'ListProduct.html'

    def get(self,request,*args,**kwargs) :
        prod_objects = Product.objects.all()
        context = {
            'list' : prod_objects
        }
        return render(request,self.template_name,context)


class EditProductView(UpdateView) :
    http_method_names = ['get','post']
    template_name = 'EditProduct.html'

    def get(self,request,pk=None) :
        products = Product.objects.get(pk=pk)
        fields_dict = {
            'productName' : products.productName,
            'category' : products.category,
            'price' : products.price,
            'quantity' : products.quantity,
            'shortDescription' : products.shortDescription,
            'longDescription' : products.longDescription
        }
        form = AddProductForm(initial=fields_dict)
        context = {'form' : form}
        return render(request,self.template_name,context)

    def post(self,request,pk=None) :
        product_obj = Product.objects.get(pk=pk)
        prod_objects = Product.objects.all()
        form = AddProductForm(request.POST,instance=product_obj)

        if form.is_valid() :
            form.save()
            context = {
                'message': 'Product Details Updated Successfully!',
                'danger': False,
                'list': prod_objects,
            }
            return render(request, 'ListProduct.html',  context)

        else :
            context = {
                'form' : form,
                'message' : 'Product Details Update Failed',
                'danger' : True,
            }
            return render(request,self.template_name,context)


class DeleteProductView(DeleteView):
    http_method_names = ['get','post']
    template_name = 'DeleteProduct.html'

    def get(self, request, pk=None):
        prod_obj = Product.objects.get(pk=pk)
        context = {'item': prod_obj}
        return render(request,self.template_name,context)

    def post(self, request, pk=None):
        prod_obj = Product.objects.get(pk=pk)
        form = AddProductForm(request.POST,instance=prod_obj)
        prod_obj.delete()
        context = {
            'message' : 'Product Deleted Successfully!!!',
            'danger' : False
        }
        return render(request,'index.html',context)

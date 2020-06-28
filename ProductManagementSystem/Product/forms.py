from django.core.exceptions import ValidationError
from django.forms import ModelForm

# App imports
from .models import Product,ProductCategory


class AddProductForm(ModelForm) :
    class Meta :
        model = Product
        fields = ['productName','category','price','quantity','shortDescription','longDescription','smallImage','largeImage']


    def clean(self) :
        """
             This method defines the Add Product form's validation.
        """
        cleaned_data = super(AddProductForm,self).clean()

        prod_price = cleaned_data.get('price')
        prod_qty = cleaned_data.get('quantity')

        if prod_price <= 0 :
            raise ValidationError("Product Price Cannot Be Zero")
        elif prod_qty <= 0 :
            raise ValidationError("Please Provide Valid Product Quantity!")
        else :
            return cleaned_data

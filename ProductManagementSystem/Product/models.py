from django.db import models


# Create your models here.

class ProductCategory(models.Model) :
    categoryName = models.CharField(max_length=30)
    categoryDescription = models.CharField(max_length=50)

    def __str__(self) :
        return self.categoryName + " " + self.categoryDescription


class Product(models.Model) :
    productName = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory,related_name='product_category',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=150)
    smallImage = models.ImageField(upload_to='Product_small_img',blank=False)
    largeImage = models.ImageField(upload_to='product_large_img',blank=False)

    def __str__(self) :
        return self.productName + " " + str(self.price)

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(
        null=True, upload_to="product_photos/"
    )  # 'upload_to' specifies the directory where images will be stored

    # Add more fields as needed

    def __str__(self):
        return self.name

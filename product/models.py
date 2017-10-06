from django.db import models

class Product(models.Model):
    '''
    model for storing products
    '''
    name = models.CharField(max_length=30, unique=True, )
    image = models.FileField(upload_to='product_image/')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
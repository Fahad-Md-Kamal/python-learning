from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

class ModelBase(models.Model):
    """ Common Fields to be inherited by all tables """
    slug = models.SlugField(max_length=255, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-created_on',)
    
    @property
    def str_creation(self):
        """ Will show the record date in humen readable format """
        return self.created_on.strftime('%d %B %Y')

    @property
    def str_updation(self):
        """ Will show the record update date in humen readable format """
        return self.updated_on.strftime('%d %B %Y')


class Category(ModelBase):
    """ Responsible for storing product Categories and Sub-category data """
    name = models.CharField(max_length=100,)
    short_description = models.TextField(max_length=300, blank=True, null=True)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='category_creator')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='category_updator')
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug =f'{slugify(self.name)}-{str(uuid.uuid4())[:8]}'
        super(Category, self).save(*args, **kwargs)



class Product (ModelBase):
    """ Responsible for storing Prduct'd data """
    category = models.ManyToManyField(Category, related_name='product_categories')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=10.00)
    is_available = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='product_creator')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='product_updator')
        
    def __str__(self) -> str:
        return self.name
    

class ProductImage(models.Model):
    """ Responsible for storing multiple images of a product """
    product = models.ForeignKey(Product, on_delete=models.Model, related_name='prod_image')
    image = models.ImageField(upload_to='product/')

    def __str__(self) -> str:
        return f'Image: {self.id} ({self.product.name})'

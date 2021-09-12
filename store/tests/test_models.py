from django.contrib.auth.models import User
from django.test import TestCase


from store import models


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = models.Category.objects.create(
            name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category Model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, models.Category))

    def test_category_url(self):
        """
        Test Category Model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        models.Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = models.Product.objects.create(
            category_id=1,
            title='django beginners',
            created_by_id=1,
            slug='django-beginners',
            price='20.00',
            image='django'
        )

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, models.Product))
        self.assertEqual(str(data), 'django beginners')

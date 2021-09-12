from unittest import skip

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpRequest

from store.models import Category, Product
from store.views import all_products


@skip("Demonstration of skipping test")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        self.prod = Product.objects.create(
            category_id=1,
            title='django beginners',
            created_by_id=1,
            slug='dj',
            price=20.00,
            image='django',
            in_stock=True
        )

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        resp = self.c.get(
            reverse('store:product_detail', args=[self.prod.slug]))

        self.assertEqual(resp.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """

        resp = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(resp.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        resp = all_products(request)
        html = resp.content.decode('utf-8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(resp.status_code, 200)

    def test_view_funtion(self):
        request = self.factory.get('/item/django-beginners')
        resp = all_products(request)
        html = resp.content.decode('utf-8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(resp.status_code, 200)

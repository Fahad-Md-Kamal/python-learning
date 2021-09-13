from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


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
            slug='django-beginners',
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

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        resp = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(resp.status_code, 400)
        resp = self.c.get('/', HTTP_HOST="yourdomain.com")
        self.assertEqual(resp.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        resp = product_all(request)
        html = resp.content.decode('utf-8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(resp.status_code, 200)

    def test_view_funtion(self):
        request = self.factory.get('/django-beginners')
        resp = product_all(request)
        html = resp.content.decode('utf-8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(resp.status_code, 200)

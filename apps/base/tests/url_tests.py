from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import *


class UrlTests(TestCase):
    def test_index_url_resolves(self):
        url = reverse('base:index')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_resolves(self):
        url = reverse('base:about')
        self.assertEqual(resolve(url).func, about)

    def test_health_check_url_resolves(self):
        url = reverse('base:up')
        self.assertEqual(resolve(url).func, up)

    def test_health_check_status_code(self):
        response = self.client.get('/up/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

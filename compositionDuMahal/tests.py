from django.test import TestCase
from django.urls import reverse # a importer
from .models import Produit, Contact, Reservation, Presentation

# Create your tests here.

class IndexPageTestCase(TestCase):
    def test_index_page(self):
        #self.assertEqual('a', 'a')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class DetailPageTestCase(TestCase):
    def test_detail_page_returns_200(self):
        impossible = Produit.objects.filter(nom="SIXO")
       #produi_id = Produit.objects.get(nom='SIXO').id
        response = self.client.get(reverse('compositionDuMahal/detail.html', ))
        self.assertEqual(response.status_code, 200)

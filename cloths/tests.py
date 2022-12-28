from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Cloth, Review


class ClothTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123',
        )

        self.cloth = Cloth.objects.create(
            style='Simple',
            stylist='MESH',
            price='25.00',
        )

        self.review = Review.objects.create(
            cloth=self.cloth,
            stylist=self.user,
            review='A great review',
        )

    def test_cloth_listing(self):
        self.assertEqual(f'{self.cloth.style}', 'Simple')
        self.assertEqual(f'{self.cloth.stylist}', 'MESH')
        self.assertEqual(f'{self.cloth.price}', '25.00')

    def test_cloth_list_view(self):
        response = self.client.get(reverse('cloth_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Simple')
        self.assertTemplateUsed(response, 'cloths/cloth_list.html')

    def test_cloth_detail_view(self):
        response = self.client.get(self.cloth.get_absolute_url())
        no_response = self.client.get('/cloths/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Simple')
        self.assertContains(response, 'A great review')
        self.assertTemplateUsed(response, 'cloths/cloth_detail.html')

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from category.models import Category
from product.models import Product
from product.serializers import ProductSerializers


class TestProductViewSet(APITestCase):

    def test_api_get_all_product(self):
        category_1 = Category.objects.create(title="title_1")
        category_2 = Category.objects.create(title="title_2")

        product_1 = Product.objects.create(title='title_product_1', price=1000, photo_url="https://test.png",
                                           description="description_product_text", category=category_1)

        product_2 = Product.objects.create(title='title_product_2', price=2000, photo_url="https://test.png",
                                           description="description_product_text", category=category_1)

        product_3 = Product.objects.create(title='title_product_3', price=1500, photo_url="https://test.png",
                                           description="description_product_text", category=category_2)

        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        data = ProductSerializers([product_1, product_2, product_3], many=True).data
        self.assertEquals(data, response.data)
        count = Product.objects.count()
        self.assertEquals(count, 3)

    def test_api_create_product(self):
        category_1 = Category.objects.create(title="title_1")
        url = reverse('product-list')

        data = {
            'title': "test_title",
            'price': 1000,
            'photo_url': "https://rrrtest.tr",
            'description': "test_description",
            'category': category_1.id
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        count = Product.objects.count()
        self.assertEquals(count, 1)


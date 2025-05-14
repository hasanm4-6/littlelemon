from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(name="Burger", price=5.99, menu_item_description=20)
        self.item2 = Menu.objects.create(name="Pasta", price=7.99, menu_item_description=15)
        self.item3 = Menu.objects.create(name="Salad", price=4.99, menu_item_description=10)
        self.client = APIClient()  

    def test_getall(self):
        response = self.client.get('/api/menu/') 

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

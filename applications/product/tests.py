from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from utils.utils import get_tokens_for_user
from applications.product.models import Product
from applications.category.models import Category


User = get_user_model()


from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile





class ProductTestCase(TestCase):
    def setUp(self) -> None:
        
        self.client = APIClient()

        user = User.objects.create(
            username='testuser',
            password='testpassword123',
            email='testuser@gmail.com',
            is_active=True
            )
        
        self.user_token = get_tokens_for_user(user)
        self.url = reverse('products-list')

        Category.objects.create(title='testcategory')
        Category.objects.create(title='okeycategory')

        self.uploaded_image = SimpleUploadedFile(
            name='Unttled.jpeg',
            content=open('/home/user/Pictures/Untitled.jpeg', 'rb').read(),
            content_type='image/jpeg'
        )

    
    


    def test_create_product_as_anonym_user(self):
        response = self.client.post(self.url, data={
            'title': 'cat', 
            'price': 123, 
            'quantity': 2, 
            'category': 'testcategory', 
            }, format='multipart', FILES={'images': self.uploaded_image})
        
        self.assertEqual(response.status_code, 401)


    def test_create_product_as_logged_in_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.user_token['access'])
        response = self.client.post(self.url, data={
            'title': 'cat', 
            'price': 123, 
            'quantity': 2, 
            'category': 'testcategory', 
            'images': self.uploaded_image
            })
        # print(response.content)

        self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        response = self.client.get(self.url).content
        print(response, 'alkdsjhglksafjhglksjhglkdsajhg')
        print(response)

        self.assertEqual(response.status_code, 200)
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shelter.models import Breed, Dog


class DogTestCase(APITestCase):
    def setUp(
            self) -> None:  # при тестировании каждый раз стирается база и создается новая. так вот setup как раз подгружает в эту базу то, тчо нам нужно для дальнейшего тестирования
        self.breed = Breed.objects.create(breed='testbreed')
        self.dog = Dog.objects.create(name='testdog', breed=self.breed)

    def test_get_list(self): # в одном тесте может быть МАКСИМУМ 1-2 ассерта
        """test for dog list"""
        # response = self.client.get('/dog/')
        response = self.client.get(
            reverse('shelter:dog_list')  # когда используем реверс, сначала название приложения, потом endpoint name
        )
        # проверяем что нет ошибок вывода страницы
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # проверяем структуру вывода
        # print(response.json())
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": "testdog",
                        "breed": "testbreed",
                        "author": None
                    }
                ]
            }
        )

    def test_dog_create(self):
        """test for dog create"""

        data = {
            'name': 'testdog2',
            'breed': self.breed.id
        }
        response = self.client.post(reverse('shelter:create_dog'), data=data)

        # проверяем что нет ошибок вывода страницы
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверяем что после создания теперь 2 собаки (одна в сетапе)
        self.assertEqual(
            Dog.objects.all().count(),
            2
        )

    def test_dog_create_validation(self):
        """test for validation within dog create"""

        data = {
            'name': 'ПРОДАМ собачку',
            'breed': self.breed.id
        }
        response = self.client.post(reverse('shelter:create_dog'), data=data)

        # проверяем что нет ошибок вывода страницы
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # проверяем что выдается сообщение ктр мы записали
        self.assertEqual(
            response.json(),
            {'name': ['SCAM_WORDS!!!']}
        )

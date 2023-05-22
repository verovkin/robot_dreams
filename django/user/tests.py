import factory
import random
from django.test import TestCase
from user.models import User


class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_user(self):
        self.assertIsInstance(self.user, User)
        print(self.user)



class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_user_list(self):
        resp = self.client.get(f'/users/')
        self.assertEqual(resp.status_code, 200)

    def test_get_user_detail(self):
        resp = self.client.get(f'/users/{self.user.id}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name, 'yo')

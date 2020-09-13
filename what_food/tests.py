from django.test import TestCase, Client

from what_food.models import Food


class FoodModelTestCase(TestCase):
    def setUp(self):
        self.food = Food(country='test', name='test')
        self.food.save()

    def test_add_new_food_model(self):
        f = Food(country='c', name='자장면')
        f.save()

    def test_edit_food_model(self):
        self.food.country = 'w'
        self.food.save()

    def test_remove_food_model(self):
        self.food.delete()


class FoodTestCase(TestCase):
    def setUp(self):
        self.client = Client()    

    def test_view_index(self):
        self.client = Client()
        resp = self.client.get("/")
        self.assertTrue(resp.status_code,200)

    def test_view_w(self):
        self.client = Client()
        resp = self.client.get("/w")
        self.assertTrue(resp.status_code,200)

    def test_view_j(self):
        self.client = Client()
        resp = self.client.get("/j")
        self.assertTrue(resp.status_code,200)

    def test_view_c(self):
        self.client = Client()
        resp = self.client.get("/c")
        self.assertTrue(resp.status_code,200)

    def test_view_k(self):
        self.client = Client()
        resp = self.client.get("/k")
        self.assertTrue(resp.status_code,200)

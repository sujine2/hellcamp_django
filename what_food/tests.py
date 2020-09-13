from django.test import TestCase, Client


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

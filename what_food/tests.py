from django.test import TestCase, Client


class FoodTestCase(TestCase):
    def test_view_index(self):
        c = Client()
        resp = c.get("/")
        self.assertTrue(resp.status_code,200)

    def test_view_w(self):
        c = Client()
        resp = c.get("/w")
        self.assertTrue(resp.status_code,200)

    def test_view_j(self):
        c = Client()
        resp = c.get("/j")
        self.assertTrue(resp.status_code,200)

    def test_view_c(self):
        c = Client()
        resp = c.get("/c")
        self.assertTrue(resp.status_code,200)

    def test_view_k(self):
        c = Client()
        resp = c.get("/k")
        self.assertTrue(resp.status_code,200)

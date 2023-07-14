from django.test import TestCase
from django.urls import reverse


class Static(TestCase):

    def test_index(self):
        r = self.client.get(reverse('index'))
        self.assertEqual(r.status_code, 200)

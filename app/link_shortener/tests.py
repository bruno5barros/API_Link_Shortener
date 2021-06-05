from django.test import TestCase
from link_shortener import models


class ModelTest(TestCase):

    def test_create_link_shorter_str(self):
        """ Test creating a shorter link based on a link"""

        link_shorter_table = models.LinkShortener.objects.create(
            full_link='https://www.google.com/',
            hash_link='ABab123'
        )

        self.assertEqual(str(link_shorter_table), link_shorter_table.full_link)

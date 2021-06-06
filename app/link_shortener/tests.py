from django.test import TestCase
from link_shortener import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from link_shortener.serializers import LinkShortenerSerializer

LINKS_SHORTENER_URL = reverse('link_shortener:link_shortener-list')

def link_shortener_detail_url(link_shortener):
    """Return a deliver detail url"""
    return reverse('link_shortener:link_shortener-detail', args=[link_shortener])


def sample_link_shorter(**params):
    """Create a link shorter sample"""
    defaults = {
        'full_link': 'https://www.google.com/'
    }
    defaults.update(params)

    return LinkSerializer.objects.create(**defaults)


class ModelTest(TestCase):

    def test_create_link_shorter_str(self, link):
        """ Test creating a shorter link based on a link"""

        link_shorter_table = models.LinkShortener.objects.create(
            full_link=link
        )

        self.assertEqual(str(link_shorter_table), link_shorter_table.full_link)

    def test_create_link_shorter_twice_str(self):
        """ Test creating a shorter link based on a link twice"""

        link_shorter_table = models.LinkShortener.objects.create(
            full_link='https://www.google.com/'
        )

        link_shorter_table = models.LinkShortener.objects.create(
            full_link='https://www.microsoft.com/'
        )

        link_shorter_list = models.LinkShortener.objects.all();

        self.assertEqual(len(link_shorter_list), 2)


class APITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_shorted_links(self):
        """Test retrieving all links"""
        payload = {
            'full_link': 'https://www.microsoft.com/'
        }
        sample_link_shorter()
        sample_link_shorter(payload)

        res = self.client.get(LINKS_SHORTENER_URL)

        link_shorter_list = models.LinkShortener.all().order_by(-id);
        serializer = LinkShortenerSerializer(link_shorter_list, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)

    def test_shorted_links_detail(self):
        """Test viewing links detail"""
        link_shorter = sample_link_shorter()
        serializer = LinkShortenerSerializer(link_shorter)

        url = link_shortener_detail_url(link_shorter.id)
        res = self.client.get(url)

        self.assertEqual(serializer.data, res.data)

    def test_create_link_shortener(self):
        """Test create a shorter link"""
        payload = {
            'full_link': 'https://www.google.com/'
        }

        res = self.client.post(LINKS_SHORTENER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        url = link_shortener_detail_url(res.data['id'])
        res = self.client.get(url)
        self.assertEqual(payload['full_link'], res.data['full_link'])

    def test_update_link_shortener(self):
        """Test updatin links with put"""
        link_shorter = sample_link_shorter()
        payload = {
            'full_link': 'https://www.microsoft.com/'
        }

        url = link_shortener_detail_url(link_shorter.id)
        res = self.client.put(url, payload, content_type='application/json')

        link_shorter.refresh_from_db()
        res = self.client.get(url)

        self.assertEqual(payload['full_link'], res.data['full_link'])

    def test_delete_link_shortener(self):
        """Test deleting link"""
        payload = {
            'full_link': 'https://www.microsoft.com/'
        }
        sample_link_shorter()
        link_shorter = sample_link_shorter(payload)

        url = reverse('link_shortener:link_shortener-detail', kwargs={
            'pk': link_shorter.pk
        })
        self.client.delete(url)
        link_shorter_list = LinkShortener.objects.all()

        self.assertEqual(len(link_shorter_list), 1)

    def test_shorted_links_query_params(self):
        """Filter LinkShortener models by full_link"""
        payload = {
            'full_link': 'https://www.microsoft.com/'
        }
        sample_link_shorter()
        sample_link_shorter(payload)

        url = LINKS_SHORTENER_URL + '?full_link=https://www.microsoft.com/'
        res = self.client.get(url)

        self.assertEqual(len(res.data), 1)

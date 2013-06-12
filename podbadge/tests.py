__author__ = 'Flavio'

from django.test import TestCase

from django.test.client import Client

class BadgeTestCase(TestCase):

    def test_root(self):
        c = Client()

        response = c.get('/')
        self.assertEqual(response.status_code, 301)

        response = c.get('/', {'some_data': 'garbage'})
        self.assertEqual(response.status_code, 301)

    def test_badge_v2(self):
        c = Client()

        response = c.get('/v/')
        self.assertEqual(response.status_code, 404)

        response = c.get('/v/NSStringMask/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('error' in response.content)

        response = c.get('/v/aowdijaowijaowidjaowidjaowij/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

        response = c.get('/v/nsstr/ingmask/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

    def test_badge_p(self):
        c = Client()

        response = c.get('/p/')
        self.assertEqual(response.status_code, 404)

        response = c.get('/p/nsstringmask/badge.png')
        self.assertEqual(response.status_code, 200)

        response = c.get('/p/nsstringmask/badge.svg')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

        response = c.get('/p/NSStringMask/badge.png')
        self.assertEqual(response.status_code, 200)

        response = c.get('/p/NSStringMask/badge.svg')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('error' in response.content)

        response = c.get('/p/aowdijaowijaowidjaowidjaowij/badge.png')
        self.assertEqual(response.status_code, 200)

        response = c.get('/p/aowdijaowijaowidjaowidjaowij/badge.svg')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

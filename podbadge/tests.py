__author__ = 'Flavio'

from django.test import TestCase

from django.test.client import Client

class BadgeTestCase(TestCase):
    def test_badge(self):
        c = Client()

        response = c.get('/')
        self.assertEqual(response.status_code, 301)

        response = c.get('/', {'some_data': 'garbage'})
        self.assertEqual(response.status_code, 301)

        response = c.get('/v/')
        self.assertEqual(response.status_code, 404)

        response = c.get('/v/nsstringmask/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('error' in response.content)

        response = c.get('/v/NSStringMask/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('error' in response.content)

        response = c.get('/v/aowdijaowijaowidjaowidjaowij/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

        response = c.get('/v/nsstr/ingmask/badge.png')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.content)

    def setup_databases(self):
        """Overrides DjangoTestSuiteRunner"""
        pass

    def teardown_databases(self, *args):
        """Overrides DjangoTestSuiteRunner"""
        pass
"""
tests.email_verifier.get
tests.email_verifier.get_raw
~~~~~~~~~~~~~~~~~~~~~~~~
All tests for our email-verifier module.
"""


from os import environ
from unittest import TestCase

class BaseTest(TestCase):
    """A base test class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass


class EmailVerificationTest(BaseTest):

    def test_raises_general_exception_on_connection_error(self):
        from emailverifier import Client
        from emailverifier.exceptions import GeneralException

        client = Client('', 'https://api.asdgasggasgdasgdsasgdasdfadfsda.com')

        self.assertRaises(GeneralException, client.get, 'a@b.c')

    def test_raises_general_exception_on_connection_error_get_raw(self):
        from emailverifier import Client
        from emailverifier.exceptions import GeneralException

        client = Client('', 'https://api.asdgasggasgdasgdsasgdasdfadfsda.com')

        self.assertRaises(GeneralException, client.get_raw, 'a@b.c')

    def test_raises_http_error_on_error(self):
        from emailverifier import Client
        from emailverifier.exceptions import HttpException

        client = Client('')

        self.assertRaises(HttpException, client.get, 'a@b.c')

    def test_returns_email_info_data(self):
        from emailverifier import Client

        client = Client(environ.get('API_KEY'))

        self.assertEqual(client.get(
            'support@whoisxmlapi.com').email_address, 'support@whoisxmlapi.com')

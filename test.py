# -*- coding: utf-8 -*-
"""
validate-email tests
"""

import string

from random import choice, randrange
from unittest import TestCase

try:
    import DNS
    ServerError = DNS.ServerError
    DNS.DiscoverNameServers()
except ImportError:
    DNS = None

    class ServerError(Exception):
        pass

from validate_email import validate_email


class ValidationTest(TestCase):
    @staticmethod
    def gen_valid(x=0, y=100):
        def _gen_id(size=6, chars=''.join([string.ascii_letters, string.digits,
                                           '_', '-', '.', '+', ' '])):
            return ''.join(choice(chars) for _ in range(size))
        return _gen_id(randrange(x, y))

    @staticmethod
    def gen_invalid(x=0, y=100):
        def _gen_id(size=6, chars=''.join([string.ascii_letters, string.digits,
                                           '_', '-', '.', '+', ' ', '&', '$', '#'])):
            return ''.join(choice(chars) for _ in range(size))
        return _gen_id(randrange(x, y))

    def setUp(self):
        self.valid_addresses = ()
        self.invalid_addresses = ()

    def test_re_validation_valid(self):
        for email_address in self.valid_addresses:
            self.assertTrue(validate_email(email_address))

    def test_re_validation_invalid(self):
        for email_address in self.invalid_addresses:
            self.assertFalse(validate_email(email_address))

    def test_mx_validation_valid(self):
        self.assertIsNotNone(DNS, 'PyDNS must be installed to run this test!')
        for email_address in self.valid_addresses:
            self.assertTrue(validate_email(email_address, check_mx=True, verify=False))

    def test_mx_validation_invalid(self):
        self.assertIsNotNone(DNS, 'PyDNS must be installed to run this test!')
        for email_address in self.invalid_addresses:
            self.assertFalse(validate_email(email_address, check_mx=True, verify=False))

    def test_smtp_validation_valid(self):
        self.assertIsNotNone(DNS, 'PyDNS must be installed to run this test!')
        for email_address in self.valid_addresses:
            self.assertTrue(validate_email(email_address, check_mx=True, verify=True))

    def test_smtp_validation_invalid(self):
        self.assertIsNotNone(DNS, 'PyDNS must be installed to run this test!')
        for email_address in self.invalid_addresses:
            self.assertFalse(validate_email(email_address, check_mx=True, verify=True))
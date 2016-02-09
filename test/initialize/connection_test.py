from mock import Mock
from faker import Faker
from unittest import TestCase

from src.initialize.connection import FalconConnection


class FalconConnectionTest(TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_initialize_with_ip(self):
        ip = 'FOo'
        connection = FalconConnection(ip)

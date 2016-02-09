from dronekit import Vehicle
from faker import Faker
from mock import Mock, patch
from unittest import TestCase

from src.initialize.connection import FalconConnection


class FalconConnectionTest(TestCase):

    def setUp(self):
        self.fake = Faker()

    @patch('dronekit.connect')
    def test_initialize_with_ip(self, dronekit_patch):
        ip = 'ip'
        falconConnection = FalconConnection(ip)
        isinstance(Vehicle, type(falconConnection.vehicle))
        dronekit_patch.assert_called_with(ip, heartbeat_timeout=10, wait_ready=True)


from dronekit import Vehicle
from mock import patch
from unittest import TestCase

from src.initialize.connection import FalconConnection


class FalconConnectionTest(TestCase):

    @patch('dronekit.connect')
    def test_initialize_with_ip(self, dronekit_patch):
        ip = 'ip'
        falcon_connection = FalconConnection(ip)
        isinstance(Vehicle, type(falcon_connection.vehicle))
        dronekit_patch.assert_called_with(ip, heartbeat_timeout=10, wait_ready=True)

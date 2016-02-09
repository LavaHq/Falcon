import socket
import exceptions

from dronekit import connect, APIException


class FalconConnection:
    """The Main Drone Connection Module

    Attributes:
        vehicle (Vehicle): the vehicle
    """
    def __init__(self, ip, heartbeat_timeout=10):
        """
        Args:
            ip (string): The IP Address that builds the connection
            heartbeat_timeout (int): Time in seconds of the Timeout

        """
        try:
            self.vehicle = connect(ip, wait_ready=True, heartbeat_timeout=heartbeat_timeout)
        # Bad TCP connection
        except socket.error:
            print 'No server exists!'

        # Bad TTY connection
        except exceptions.OSError as e:
            print 'No serial exists! error:{0}'.format(e)

        # Timeout Error
        except APIException:
            print 'API Exception Thrown'

        # General Exception
        except Exception, e:
            print 'General Exception: {0}'.format(e)

"""We will start with the app in this file and let it evolve as neccesary
    currently we wil luse this to collect"""

from dronekit import connect

if __name__ == '__main__':
    # Connect to UDP endpoint.
    vehicle = connect('127.0.0.1:14550', wait_ready=True)

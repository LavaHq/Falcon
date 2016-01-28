from dronekit import connect, VehicleMode

from dronekit_sitl import SITL

if __name__ == '__main__':
    print "Start Simulator (SITL)"

    sitl = SITL()
    sitl.download('copter', '3.3', verbose=True)
    sitl_args = ['-IO', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
    sitl.launch(sitl_args, await_ready=True, restart=True)

    # Connect to the Vehicle
    vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

    # Get Vehicle Attributes
    print "Simultaor Statistics"
    print " GPS: {0}".format(vehicle.gps_0)
    print " Battery: {0}".format(vehicle.battery)
    print " Last Heartbeat: {0}".format(vehicle._heartbeat_lastreceived)
    print " Is Armable?: {0}".format(vehicle.is_armable)
    print " System status: {0}".format(vehicle.system_status.state)
    print " Mode: {0}".format(vehicle.mode.name)

    vehicle.close()
    sitl.stop()
    print "Le Fin"


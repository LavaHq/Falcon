print "Start Simulator (SITL)"
from dronekit_sitl import SITL

sitl = SITL()
sitl.download('copter', '3.3', verbose=True)
sitl_args = ['-IO', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
sitl.launch(sitl_args, await_ready=True, restart=True)
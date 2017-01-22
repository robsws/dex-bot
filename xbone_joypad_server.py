import xmlrpclib 
from SimpleXMLRPCServer import SimpleXMLRPCServer
from gopigo import *

throttle_multiplier = 20
turn_multiplier = 10

def move_robot(turn, forward):
  print(str(forward) + "," + str(turn))
  # throttle
  forward *= throttle_multiplier
  turn *= turn_multiplier
  if forward < 0:
    fwd()
  elif forward > 0:
    bwd()
  else:
    stop()
  set_speed(abs(forward))
  # turning
  if turn < 0:
    # turn left
    set_right_speed(abs(forward) + abs(turn))
    set_left_speed(abs(forward) - abs(turn))
  elif turn > 0:
    # turn right
    set_right_speed(abs(forward) - abs(turn))
    set_left_speed(abs(forward) + abs(turn))
  return 1

server = SimpleXMLRPCServer(("dex.local", 8000))
print("Listening on port 8000")
server.register_function(move_robot, "move_robot")
server.serve_forever()

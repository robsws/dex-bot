import xmlrpclib 
from SimpleXMLRPCServer import SimpleXMLRPCServer
from gopigo import *

throttle_multiplier = 2
turn_multiplier = 1

def move_robot(turn, forward):
  print(str(forward) + "," + str(turn))
  # throttle
  if forward < 0:
    fwd()
  elif forward > 0:
    bwd()
  else:
    stop()
  set_speed(abs(forward)*speed_multiplier)
  # turning
  if turn < 0:
    # turn left
    set_right_speed(abs(forward) + abs(turn) * turn_multiplier)
    set_left_speed(abs(forward) - abs(turn) * turn_multiplier)
  elif turn > 0:
    # turn right
    set_right_speed(abs(forward) - abs(turn) * turn_multiplier)
    set_left_speed(abs(forward) + abs(turn) * turn_multiplier)
  return 1

server = SimpleXMLRPCServer(("dex.local", 8000))
print("Listening on port 8000")
server.register_function(move_robot, "move_robot")
server.serve_forever()
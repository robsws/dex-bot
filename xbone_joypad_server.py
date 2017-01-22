import xmlrpclib 
from SimpleXMLRPCServer import SimpleXMLRPCServer
from gopigo import *

def move_robot(turn, forward):
  print(str(forward) + "," + str(turn))
  if forward < 0:
    fwd()
  elif forward > 0:
    bwd()
  else:
    stop()
  set_speed(abs(forward))
  return 1

server = SimpleXMLRPCServer(("dex.local", 8000))
print("Listening on port 8000")
server.register_function(move_robot, "move_robot")
server.serve_forever()
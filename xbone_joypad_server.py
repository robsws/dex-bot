from xmlrpc.server import SimpleXMLRPCServer
# from gopigo import *

def move_robot(x, y):
  print(str(x) + "," + str(y))
  return 1

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000")
server.register_function(move_robot, "move_robot")
server.serve_forever()
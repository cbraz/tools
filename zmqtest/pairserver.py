import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
i=0
while i<10000:
    socket.send_string("Server message to client3")
    msg = socket.recv()
    print (msg)
    i+=1
#    time.sleep(1)

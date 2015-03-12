import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)
#socket.connect("tcp://192.168.1.150:%s" % port)
i=0
while True:
    msg = socket.recv()
    print (msg)
    socket.send_string("client message to server1")
    i+=1
    print(i)
#    socket.send_string("client message to server2")
#    time.sleep(1)

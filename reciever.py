import time
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.DEALER)
identity = u'receiver'
socket.identity = identity.encode('utf-8')
socket.connect('ipc://router')
print('Client %s started' % (identity))
while True:
    msg = socket.recv()
    print('Client received: %s' % msg)

socket.close()
context.term()
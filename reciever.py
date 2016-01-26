import time
import zmq
from converter import binary_to_dict
import time

context = zmq.Context()
socket = context.socket(zmq.DEALER)
identity = u'receiver'
socket.identity = identity.encode('utf-8')
socket.connect('ipc://router')
print('Client %s started' % (identity))
while True:
    msg = socket.recv()
    print('Client received: %s' % binary_to_dict(msg))

socket.close()
context.term()
import time
import zmq
from converter import pack_message
import time

context = zmq.Context()
socket = context.socket(zmq.DEALER)
identity = u'sender'
socket.identity = identity.encode('utf-8')
socket.connect('ipc://router')
print('Client %s started' % (identity))
reqs = 0
while True:
    reqs = reqs + 1
    print('Req #%d sent..' % (reqs))
    socket.send(pack_message("receiver",reqs))
    time.sleep(1)

socket.close()
context.term()
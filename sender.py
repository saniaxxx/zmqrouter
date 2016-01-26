import time
import zmq
from converter import dict_to_binary,binary_to_dict
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
    message = {"message":reqs,"to":'receiver'}
    socket.send(dict_to_binary(message))
    time.sleep(1)

socket.close()
context.term()
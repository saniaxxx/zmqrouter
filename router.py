import time
import zmq
from converter import dict_to_binary,binary_to_dict

context = zmq.Context()
router = context.socket(zmq.ROUTER)
router.bind("ipc://router")
working = True
print("router started")
while working:
	ident, msg = router.recv_multipart()
	message_dict = binary_to_dict(msg)
	message_to_send = dict_to_binary({"from":str(ident, 'utf-8'),"message":message_dict["message"]})
	router.send_multipart([bytes(message_dict["to"],'utf-8'), message_to_send])
router.close()
context.term()
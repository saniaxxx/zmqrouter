import time
import zmq
from converter import unpack_message

context = zmq.Context()
router = context.socket(zmq.ROUTER)
router.bind("ipc://router")
print("router started")
while True:
	ident, pure_msg = router.recv_multipart()
	router.send_multipart(unpack_message(pure_msg))
router.close()
context.term()
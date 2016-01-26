import json

identity_lenght = 10

def pack_message(to,message):
	return bytes(normalize_identity(to)+str(message),'utf-8')

def unpack_message(the_binary):
	message_str = str(the_binary,'utf-8')
	to = bytes(strip_identity(message_str[:identity_lenght]),'utf-8')
	message = bytes(message_str[identity_lenght:],'utf-8')
	return (to,message)

def normalize_identity(identity):
	return identity.zfill(identity_lenght)

def strip_identity(identity):
	return identity.lstrip('0')
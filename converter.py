import json

def dict_to_binary(the_dict):
    string = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in string)
    return bytes(binary, 'utf-8')


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d
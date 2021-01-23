from base64 import *
def EncodeB64(text_to_encode:str):
    bytes_msg = text_to_encode.encode('ascii')
    b64_bytes = b64encode(bytes_msg)
    return b64_bytes.decode('ascii')
def DecodeB64(text_to_decode:str):
  b64_b =  text_to_decode.encode('ascii')
  msg_b = b64decode(b64_b)
  return msg_b.decode('ascii')
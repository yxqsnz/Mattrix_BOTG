import random,string
from hashlib import md5 as hmd5
def GenHashmd10(text):
    alphabetarr = list(string.ascii_letters)
    hashc = []
    for i in range(0, len(alphabetarr)):
        hashc.append(random.choice(alphabetarr))
    for i in range(0, 12):
        hashc.append(random.randint(0, 9))
    r=""
    for i in range(0, len(hashc)):
        r+=str(hashc[i])
    return str(hmd5(f'{r}'.encode()).hexdigest())[:len(str(hmd5(f'{r}'.encode()).hexdigest()))] + str(hmd5(f'{r}'.encode()).hexdigest())[34:] + str(hmd5(f"{text}".encode()).hexdigest())[5:]


def GenHashmd5(toencode):

    return str(hmd5(f'{toencode}'.encode()).hexdigest())




#!/usr/bin/python

__author__ = "bt3gl"
__email__ = "bt3gl@gmail.com"


import decimal
import socket




def bs_paillier(lo, hi, s):
    if hi < lo: return None
    mid = (hi + lo) // 2
    print("We are at: ")
    print(mid)

    s.send(b'E')
    s.recv(4096)
    s.send(str(mid)[:-1])
    ans = s.recv(4096)

    if 'None' in ans:
        print "Found it!"
        return mid + 1
    elif 'Your secret' in ans:
        return bs_paillier(lo, mid-1, s)
    else:
        return bs_paillier(mid+1, hi, s)




def get_mod_paillier():

    # create socket, answer first question
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.recv(4096)
    s.send(b'paillier')
    s.recv(4096)

    # start binary search
    hi = pow(11,307)
    lo = pow(10,307)
    mod = bs_paillier(lo, hi, s)
    print mod



if __name__ == "__main__":

    PORT = 12445
    HOST = 'asis-ctf.ir'

    get_mod_paillier()






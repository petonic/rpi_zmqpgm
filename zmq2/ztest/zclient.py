#!/usr/bin/env python

import zmq

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, '')
    # Python3 Note: Use the below line and comment
    # the above line out
    # socket.setsockopt_string(zmq.SUBSCRIBE, '')
    socket.connect("epgm://224.0.0.1:8200")

    while True:
        msg = socket.recv()
        # Python3 Note: Use the below line and comment
        # the above line out
        # msg = socket.recv_string()
        print(msg)

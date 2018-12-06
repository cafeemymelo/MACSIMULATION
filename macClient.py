#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: package importing
import socket
import threading
import numpy as np

class MacSimulation:

    # TODO: variable declaration


    def __init__(self, host, port):
        self.receive_message = list()
        # create the TCP/IP socket
        self.node_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the nodeClient to the port where the nodeServer is listening
        self.node_client.connect((host, port))
        t = threading.Thread(target=self.runClientOnServer)
        t.start()

    def runClientOnServer(self):

        while self.node_client is not None:
            try:
                message = self.node_client.recv(4096)
                message = str(message)
                if int(len(message)) > 0:
                    self.receive_message.append(message)
            finally:
                pass

    def getMessage(self):

        if len(self.receive_message) > 0:
            message = self.receive_message[0]
            del self.receive_message[0]
        else:
            message = None
        return message

    def setMessage(self, message):
        self.node_client.sendall(message.encode())

    def getRSSI(self):
        return np.random.randint(0,100)
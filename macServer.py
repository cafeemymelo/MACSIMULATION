# TODO: Package Importing
import socket
import threading



# TODO: Variable declaration
PORT = 10000
HostAddress = "localhost"
keep_listening = True
threadsServer = list()
clients = list()

# TODO: Creating the server
# create a TCP server
server_Node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Prepares server to wait for client connection
server_Node.bind(("localhost", 7000))
# Listening the clients
server_Node.listen(4)

def runClientOnServer(connection,client_address):
    global keep_listening
    while keep_listening == True:
        try:
            message = connection.recv(120)
            print("Received message:", message)
            if len(message) <= 0:
                print("Client", client_address, "closed the connection.")
                connection.close()
                keep_listening = False
                break
            else:
                for c in clients:
                    if c[1] != client_address:
                        c[0].send(message)

        finally:
            pass


#TODO:
def WaitingForClients():
    global clients
    try:
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = server_Node.accept()
            clients.append(list([connection,client_address]))
            t = threading.Thread(target=runClientOnServer, args=(connection, client_address))
            t.start()
            threadsServer.append(t)
    finally:
        server_Node.close()
t = threading.Thread(target=WaitingForClients)
t.start()
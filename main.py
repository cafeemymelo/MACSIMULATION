import time

from macClient import MacSimulation

clientNum = 3
client = list()

for c in range(clientNum):
    client.append(MacSimulation("localhost",7000))

while True:
    for c in range(clientNum):
        client[c].setMessage(str(c) + "hello")
        message = client[c].getMessage()
        while message is not None:
            print(str(c) + ": " + message)
            message = client[c].getMessage()
            time.sleep(1)
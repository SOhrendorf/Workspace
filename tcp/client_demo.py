import socket
import time

while True:  # infinite loop until socket can connect
    try:
        print("Connecting...")
        objSocket = socket.socket()
        objSocket.connect(("127.0.0.1", 56213))
    except socket.error:
        print("couldnt connect")
        time.sleep(10)  # wait 10 seconds to try again
    else:
        break
objSocket.send(str.encode("TEST"))

# John wood
# Aug 31, 2020
# this example is on freecodecamp
# Sockets
import socket
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try:
connectionSocket.connect(('data.pr4e.org', 80))
#except:
#    print('Failed to connect')
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
connectionSocket.send(cmd)

while True:
    data = connectionSocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
connectionSocket.close()


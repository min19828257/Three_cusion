from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.35.9', 8080))

print('연결 확인 됐습니다.')

li = '1,2,3,4,5,6,0,0,0,10,10,10,10,0'
clientSock.send(li.encode('utf-8'))

print('메시지를 전송했습니다.')

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

from socket import *

def data_receive(x,y):

    result = str(x)+","+str(y)+',3,4,5,6,0,0,0,10,10,10,10,0'
    print("result : ", result)
    return result

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.35.9', 8080))

li_x = [3,5,0,0,10,10 ]
li_y = [4,6,0,10,10,0 ]
print('연결 확인 됐습니다.')
    
li = data_receive(li_x[5],li_y[5])
clientSock.send(li.encode('utf-8'))

print('메시지를 전송했습니다.')

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

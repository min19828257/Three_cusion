from socket import *

class Data_base:
    
    def __init__(self):
        r_data = "None"

    def Setting(self,data):
        self.r_data = data
        self.r_data = data

    def Get(self):
        return self.r_data

def transform(data):
    Data_base.Setting(data)

def Setting():
    data = Data_base.Get()
    print("DB data : ", DB.Get())
    return data

def socket_set(ip,port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind((ip, port))
    serverSock.listen(1)

    connectionSock, addr = serverSock.accept()

    print(str(addr),'에서 접속이 확인되었습니다.')

    data = connectionSock.recv(1024).decode('utf-8')
    transform(data)

    answer = "None"
    print("기존 앤써 : ",answer)
    while(answer == "None"):
        answer = Setting()
    print("받은 앤써 : ",answer)

    connectionSock.send(answer.encode('utf-8'))
    print('메시지를 보냈습니다.')

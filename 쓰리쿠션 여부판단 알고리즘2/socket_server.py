from socket import *
import check_cusion

def transform(data):
    sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c = check_cusion.classify(data)
    result = check_cusion.cusion_check(sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c)
    return result

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
    answer = transform(data)

    connectionSock.send(answer.encode('utf-8'))
    print('메시지를 보냈습니다.')

socket_set('192.168.35.9',8080)

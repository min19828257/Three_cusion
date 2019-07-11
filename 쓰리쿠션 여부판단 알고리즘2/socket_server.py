from socket import *
import check_cusion

#받아온 데이터를 수구,적구1,적구2,사각지점들로 분류하기
def classi(data):
    sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c = check_cusion.classify(data)
    return sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c

#각각의 데이터를 이용해 쿠션 체크하기
def Check(sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c):
    result = check_cusion.cusion_check(sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c)
    return result

def socket_set(ip,port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind((ip, port))
    serverSock.listen(1)

    connectionSock, addr = serverSock.accept()

    print(str(addr),'에서 접속이 확인되었습니다.')

    data = connectionSock.recv(1024).decode('utf-8')
    
    sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c = classi(data)
    answer = Check(sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c)
    answer = str(answer)

    connectionSock.send(answer.encode('utf-8'))
    print('메시지를 보냈습니다.')

socket_set('210.119.88.174',8080)

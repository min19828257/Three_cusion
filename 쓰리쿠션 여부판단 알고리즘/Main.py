import socket_server
import check_cusion
import DB

instance = socket_server.Data_base()

socket_server.socket_set('192.168.35.9',8080)
data = instance.Get()
sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c = check_cusion.classify(data)
result = check_cusion.cusion_check(sg,jg1,jg2,l_b_c,l_t_c,r_t_c,r_b_c)
print("data : ",result)
instance.Setting(result)

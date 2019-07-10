#쿠션여부 카운팅
class Cusion:
    wall_cnt=0
    ball_cnt=0

#받은 데이터를 수구,적구2개,사각지점으로 분류하기
def classify(data):
    data_ = data.split(",")
    soogoo = data_[:2]
    jukgoo1 = data_[2:4]
    jukgoo2 = data_[4:6]

    left_bottom_corner = data_[6:8]
    left_top_corner = data_[8:10]
    right_top_corner = data_[10:12]
    right_bottom_corner = data_[12:14]

    print("right_t_c",right_top_corner)
    print("right_b_c",right_bottom_corner)

    return soogoo,jukgoo1,jukgoo2,left_bottom_corner,left_top_corner,right_top_corner,right_bottom_corner

def cusion_check(soogoo,jukgoo1,jukgoo2,left_bottom_corner,left_top_corner,right_top_corner,right_bottom_corner):
    #1.수구 적구충돌여부확인
    check_collision(soogoo,jukgoo1,jukgoo2)
    #2.사각지점 통해 수구가 벽을 3번맞췄는가
    check_wall(soogoo,left_bottom_corner,left_top_corner,right_top_corner,right_bottom_corner)

    #3.쿠션의 조건이 맞나 result 1(성공) -1(실패)
    resullt = confirm()
    
    if(result == 1):
        return 1
    else:
        return 2


#1.수구 적구충돌여부확인
def check_collision(soogoo,jukgoo1,jukgoo2):
    distance1 = int(soogoo) - int(jukgoo1)
    distance2 = int(soogoo) - int(jukgoo2)

    if(distance1 == 0 | distance2 == 0):
        Cusion.ball_cnt += 1

#2.사각지점 통해 수구가 벽을 3번맞췄는가
def check_wall(soogoo,left_bottom_corner,left_top_corner,right_top_corner,right_bottom_corner):
    # 각각의 당구공 x,y좌표들을 계산해야
    distance_soogoo_l_b_c = int(soogoo) - int(left_bottom_corner)
    distance_soogoo_l_t_c = int(soogoo) - int(left_top_corner)
    distance_soogoo_r_t_c = int(soogoo) - int(right_top_corner)
    distance_soogoo_r_b_c = int(soogoo) - int(right_botoom_corner)

    if(distance_soogoo_r_b_c == 0 | distance_soogoo_r_t_c == 0 | distance_soogoo_l_t_c==0 | distance_soogoo_l_b_c==0):
        Cusion.wall_cnt += 1

#3.쿠션의 조건이 맞나 result 1(성공) -1(실패)
def confirm(self):
    if(Cusion.ball_cnt > 1):
        print("공 충돌2번 오케이")
        if(Cusion.wall_cnt > 2):
            print("벽 충돌3번 오케이 쓰리쿠션 성공")
            Cusion.wall_cnt=0;Cusion.ball_cnt=0
            return 1
    else:
        print("공 충돌 실패")
        return -1


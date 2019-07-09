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
    #2.사각지점 통해 수구가 벽을 3번맞췄는가
    #3.쿠션의 조건이 맞나
    result = "1"

    return result

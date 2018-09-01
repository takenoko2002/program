
#ハノイの塔の問題を解く

def move(k,start=1,yobi=2,end=3):
    if k >= 2:
        move(k-1,start,end,yobi)
    print(start,"軸の円盤を",end,"軸に移動します。")
    if k >= 2:
        move(k-1,yobi,start,end)

#ハノイの円盤の数
k = 4

move(k,1,2,3)
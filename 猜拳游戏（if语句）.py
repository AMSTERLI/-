'''
步骤：
1，出拳
    玩家：手动输入
    电脑：随机（已写好）
2，判断输赢
    玩家获胜
    平局（出同样的手势）
    电脑获胜
'''
import random
player=int(input("请出拳：1--石头;2--剪刀;3--布:"))
computer= random.randint(1,3)
print(computer)
if player==computer:
    print("平局，不服再战")
elif ((player==1)and(computer==2)) or ((player==2) and (computer==3)) or ((player==3) and (computer==1)) :
    print("你赢了，害~~~")
else:
    print("你输了,哈哈哈哈哈")


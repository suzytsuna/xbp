print ("チームの勝敗がかかったＰＫ！さあ、どうする！？")
name=input("プレーヤーの名前を入れてください")
print(name,"さんはキーパーです")

c=0
for i in range (3):
    print(i,"回目")
   
    a=int(input("1,右2,真ん中3,左の中で好きな数字を選んでね"))
    print(a)
    import random
    b =int( random.randint(1, 3))
    print(b)
    if a==b:#コンピューターと同じ数字を選んだ
        c=c+1
        print("とめた！")
    else:#違う数字を選んだ
        print("逃した...")
    if c>=2:#３回中２回以上勝った
        print("おめでとう！あなたはチームを勝利へ導いた英雄として称えられた！！")
    else:#３回中２回負けた
        print("残念、もう一度このゲームにチャレンジしよう！")
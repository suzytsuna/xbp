for i in range(4):
    print(i,("人目"))
    #文字だからダブルクォーテーションマークを入れた。
    name=input("名前を入れてください")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))
    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=45:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")

for i in range (3):
    print(i,"回目")
   
    b=int(input("0~5の中で好きな数字を選んでね"))
    print(b)
    import random
    a =int( random.randint(0, 5))
    print(a)
    if a==b:
        print("You WIN!!")
    else:
        print("You LOST")
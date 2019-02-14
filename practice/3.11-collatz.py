def collatz(number) :
    if (number % 2) == 0 :
        print(number // 2)
    elif (number % 2) == 1 :
        print(number * 3 + 1)

number = input()
try:
    # 如果number是非整数，则int()会报ValueError的错 
    collatz(int(number))
except ValueError:
    print("请输入一个整数！")


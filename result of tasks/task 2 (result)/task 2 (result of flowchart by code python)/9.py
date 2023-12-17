Min = 0
Max = input("please enter your number : ")
count = 0
storage = 0

while int(Max) > Min:
    Min = Min + 1
    if Min % 2 == 1:
        print("your number is odd" + '(' + str(Min) + ')')
        storage = storage + Min
        count = count + 1
print("total of number is :", storage)
print("counting :", count)

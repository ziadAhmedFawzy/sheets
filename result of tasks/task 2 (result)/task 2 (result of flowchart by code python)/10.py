count, stor, ave = 0, 0, 0

while count < 7:
    count += 1
    num = input("please enter your num" + str(count) + ": ")
    stor = stor + int(num)

ave = stor / 7
print(ave)

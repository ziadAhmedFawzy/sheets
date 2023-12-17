count, _sum = 0, 0

while count < 4:
    count += 1
    sub = input("please enter your subject: ")
    _sum = _sum + int(sub)

ave = _sum / 4

if ave >= 60:
    print("you are passed")
else:
    print("you are fail")

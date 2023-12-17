n_min, _sum = 0, 0
n_max = 10

while n_min < n_max:
    n_min += 1
    n = input("please enter your num" + str(n_min) + ": ")
    _sum = _sum + int(n)

print("your sum is (" + str(_sum) + ")")

hour = input("enter hours : ")
rate = input("enter rate : ")
# I converted and calculated the average to a fractional number because
# one of the possibilities is that the hours or the average are fractional,
# so I converted it so that no error occurs.
pay = float(hour) * float(rate)
print(pay)

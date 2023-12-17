from math import *

s1 = input("pleas enter your side 1 :")
s2 = input("pleas enter your side 2 :")
s3 = input("pleas enter your side 3 :")

half_tri = (int(s1) + int(s2) + int(s3)) / 2

area = sqrt(half_tri * (half_tri - int(s1)) * (half_tri - int(s2)) * (half_tri - int(s3)))

parameter = int(s1) + int(s2) + int(s3)

print("this is area of circle : " + str(area)) 
print("this is parameter of circle : " + str(parameter))
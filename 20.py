import math
a=int(input("enter coefficent of x^2"))
b=int(input("enter coefficent of x"))
c=int(input("enter constant"))
d=math.pow(b, 2)-4*(a*c)
if d<0:
  print("roots are imaginary")
else:
  print("roots are real")
r1=(-b+math.pow(d, 1/2))/2*a
r2=(-b-math.pow(d, 1/2))/2*a
print("root1=",r1)
print("root2=",r2)

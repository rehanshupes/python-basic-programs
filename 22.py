d=int(input("Enter day:"))
m=int(input("Enter month:"))
y=int(input("Enter year:"))
print("Next date:\n")
if y%4==0:
    if d>=28 & m==2:
        print("Day=",1,"Month=",m+1,"Year=",y)
    if d==31 & m==1 | m==3 | m==5 | m==7 | m==8 | m==10 | m==12:
        print("Day=",1,"Month=",m+1,"Year=",y)
    if d==30 & m==4 | m==6 | m==9 | m==11:
        print("Day=",1,"Month=",m+1,"Year=",y)
    else:
        print("Day=",d+1,"Month=",m,"Year=",y)
else:
    if d==31 & m==1 | m==3 | m==5 | m==7 | m==8 | m==10 | m==12:
        print("Day=",1,"Month=",m+1,"Year=",y)
    if d==30 & m==4 | m==6 | m==9 | m==11:
        print("Day=",1,"Month=",m+1,"Year=",y)
    else:
        print("Day=",d+1,"Month=",m,"Year=",y)


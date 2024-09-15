a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
opr=input("Enter a opr(+,-,*,/)")
if(opr=="+"):
    print(a+b)
elif(opr=="-"):
    print(a-b)
elif(opr=="*"):
    print(a*b)
elif(opr=="/"):
    print(a/b)
else:
    print("invalid opr")
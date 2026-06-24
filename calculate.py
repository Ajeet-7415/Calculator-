a=float(input("enter a number"))
op = input("enter op")
b=float(input("enter b number "))

if(op=="+"):
    print("addition=",a+b)
elif(op=="-"):
    print("subtraction=",a-b)
elif(op=="*"):
    print("multification",a*b)
elif(op=="/"):
    print("division",a/b)
elif(op=="//"):
    print("for division",a//b)
elif(op=="%"):
    print("moduls",a%b)
elif(op=="**"):
    print("expontial",a**b)
else:
    print("invalid op")
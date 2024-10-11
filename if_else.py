no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))
no3=int(input("Enter No3:"))

if no1>0 and no2>0 and no3>0 :
    if no1>no2 and no1>no3:
        print(no1,"is maximum number")
    elif no2>no1 and no2>no3 :
        print(no2,"is maximum number")
    else :
        print(no3,"is maximum number")
else :
    print("Invalid Input")

    print("outside if")
rollno=int(input("Enter Roll No:"))
name=input("Enter Name :")
maths=int(input("Enter Maths Marks:"))
if not  0<=maths<=100 :
    print("\n invalid marks")
    maths=int(input("Enter Maths Marks:"))

science=int(input("Enter Science Marks:"))
if not  0<=science<=100 :
    print("\n invalid marks")
    science=int(input("Enter Science Marks:"))

english=int(input("Enter English Marks:"))
if not  0<=english<=100 :
    print("\n invalid marks")
    english=int(input("Enter English Marks:"))



print("\n Output :\n");
print("Roll No:",rollno)
print("Name:",name)
print("Maths :",maths)
print("Science :",science)
print("English :",english)

if maths>33 and science>33 and english>33:
    total=maths+science+english
    avg=total/3
    print("total :",total)
    print("Avg:",avg)
    if avg>90:
        print("Grade : A")
    elif avg>75:
        print("Grade : B")
    elif avg>65:
        print("Grade : C")
    else :
        print("Grade :D")

    print("You are Pass")
else :
    print("You are Fail")


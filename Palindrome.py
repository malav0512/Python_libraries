
start=int(input("Enter starting no :"))
end=int(input("Enter ending number :"))

for no in range(start,end):
    if no>99:
      if (no%10)==((no//10)//10):
       print(no)
    else:
     if (no%10)==(no//10):
      print(no)







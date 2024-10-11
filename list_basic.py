no=list()
n=int(input("Enter the number of range:"))
for i in range (n):
    no.append(int(input("Enter the value:")))

print("Length of list is :",len(no))
print("The last item of list is:",no[-1])
no.sort()
no.reverse()
print("The reverse order of list is:",no)
if 5 in no:
  print("Yes")
else:
 print("No")
if no[i]%5==0:
     print(no[i])
no.remove(no[0])
no.remove(no[-1])
no.sort()
print("The result is :",no)
print("The number of 5 is :",no.count(5))
sum=0
for i in no:
 if i<5:
  sum=sum+1
print("sum:",sum)



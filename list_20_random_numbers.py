no=list()
for count in range (20):
  no.append(int(input("Enter the value in the given range(1-100):")))
print(no)
print("The average of these numbers is : ",sum(no)/20)
print("The largest element in the list is :",max(no))
print("The smallest number in the list is :",min(no))
i=no[:]
i.remove(max(i))
i.remove(min(i))
print("The second largest element in the list is:",max(i))
print("The second smallest number in the list is :",min(i))
count=0
for element in no:
 if element%2==0:
  count=count+1
print("No of even numbers:",count)



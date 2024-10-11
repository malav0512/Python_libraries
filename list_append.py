no=list()
rang=int(input("Enter the range:"))
for element in range(rang):
    no.append(int(input("Enter the value betn 1 to 12:")))
for i in range (rang):
 if no[i]>10:
  no.remove(no[i])
  no.insert(i,10)
print(no)
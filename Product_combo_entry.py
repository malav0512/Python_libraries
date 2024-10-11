' Product combo entry  product:pizza,,burger,sandwich,pasta,coke. '
'''
[s1(),233]
combo 1: pizza +fries+burger+coke==$5
combo 2: pizza +sandwich+burger+coke=$10
combo 3: burger+sandwich+pasta+coke=$7
If any thing extra needed the $5 would be charged
'''
print("\t\t Pizzarian \t\t")
print("")
print("\tcombo : pizza +sandwich+burger+coke=$15\t\t")

class pizzerian:

 def __init__(self):
     self.pizza=0
     self.burger=0
     self.sandwich=0
     self.coke=0
     self.combo=0

pizzerian_list=[]
sum=0
no=int(input("Enter the number of data entry:"))
for i in range(no):
    s1=pizzerian()
    print("Data entry:",i+1)
    s1.pizza=int(input("Enter the number of pizza:"))
    s1.burger=int(input("Enter the number of burger:"))
    s1.sandwich=int(input("Enter the number of sandwich:"))
    s1.coke=int(input("Enter the number of coke:"))
    s1.combo=int(input("Enter the number of combo meals :"))
    pizzerian_list.append(s1)


for pizzerian in pizzerian_list:
    print("\tPizza:",pizzerian.pizza)
    print("\tBurger:",pizzerian.burger)
    print("\tSandwich:",pizzerian.sandwich)
    print("\tCoke:",pizzerian.coke)
    print("\tCombo:",pizzerian.combo)
    sum = (s1.pizza * 10) + (s1.burger * 5) + (s1.sandwich * 5) + (s1.coke * 1) + (s1.combo * 15)
    print("Bill:",sum)

    print("Visit Again")



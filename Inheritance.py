class Personal_info():
    id=""
    name=""
    address=""
    phno=""

    def set_personal_info(self):
        self.id=(int(input("Enter id:")))
        self.name=(input("Enter Name:"))
        self.address=(input("Enter address:"))
        self.phno=(int(input("Enter phno:")))

    def get_personal_info(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Address:",self.address)
        print("Phone num:",self.phno)

class Customer(Personal_info):
    billamount=0
    discount=0

    def set_customer(self):
        self.set_personal_info()
        self.billamount=(int(input("Enter bill amount:")))
        self.discount=(int(input("Enter discount:")))

    def get_customer(self):
        self.get_personal_info()
        print("Bill amount:",self.billamount)
        print("Discount:",self.discount)

class Employee(Personal_info):
    salary=0

    def set_salary(self):
        self.set_personal_info()
        self.salary=(int(input("Enter salary:")))

    def get_salary(self):
        self.get_personal_info()
        print("Salary:",self.salary)

class DMart(Customer):
    location=""
    branch=""

    def setValue(self):
        self.branch=(input("Enter branch:"))
        self.location=(input("Enter location:"))

    def getValue(self):
        print("Branch:",self.branch)
        print("Loaction:",self.location)

dmart=DMart()
dmart.setValue()
dmart.set_customer()
dmart.set_salary()
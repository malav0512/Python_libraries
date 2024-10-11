class student:

  def __init__(self):
    self.rollno = None
    self.maths = 0
    self.sci = 0
    self.result=""

student_list=[]
for i in range(2):
    s1=student()
    s1.rollno = int(input("Enter Roll No:"))
    s1.maths=int(input("Enter Maths marks:"))
    s1.sci=int(input("Enter Science Marks:"))
    if s1.maths>35 and s1.sci>35:
        s1.result="Pass"
    else:
        s1.result="Fail"
    student_list.append(s1)
for student in student_list:
    print("Roll NO:",student.rollno)
    print("Maths :",student.maths)
    print("Science :",student.sci)
    print("Result:",student.result)

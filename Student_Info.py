#Task: To get the student data through keyboard and store it in an excel file (.csv) exctension
import csv

def csv_write(student):
    with open("Student_Info.csv","a",newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Phone","Email"])
        writer.writerow(student)

count=1

while True:    
    student_info=input("Enter student {} information as (Name,Age,Phone,E-Mail)".format(count))
    student=student_info.split(",")
    print("Name: {}\nAge: {}\nPhone: {}\nEmail: {}".format(student[0],student[1],student[2],student[3]))
    num=list[1:11]
    
    try:
        if ((len(student[0])>=3) and ((int(student[1])<=100 and int(student[1])>=3)) and ((int(student[2])>=0) and (len(student[2])==10)) and ("@" in student[3] and ".com" in student[3])):
            correct=input("Is that entered information correct?(yes(y)/no(n)):")
            
            if correct=="yes" or correct=="y":
                csv_write(student)
                condition=input("Do you want to add another info(yes(y)/no(n)):")
                
                if condition=="yes" or condition=="y":
                    count+=1
                    
                elif condition=="no" or condition=="n":
                    break
                    
            elif correct=="no" or correct=="n":
                print("Re-Enter the values!!")
                
        else:
            print("The Above Entered values are incorrect, Re-Enter the values!!")
            
    except(Exception):
        print("The Above Entered values are incorrect, Re-Enter the values!!")

print("Thank you for using our application, now check the excel file for the result")

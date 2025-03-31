# creating a dictionary and adding data

Student = {'Alice':80,'Bin':78,'Bob':99}
name = input("Enter Student name : ")

if name in Student:
    print(name + "'s marks: " + str(Student[name]))

else:
    print("Name Not Found")
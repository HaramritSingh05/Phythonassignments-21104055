print("\n\nQuestion 6 : Dictionary functions and sorting.\n")
program_flow = True
user_data={}
while(program_flow):
    student_name = input("Enter name : ")
    input_ok = False
    while(input_ok == False):
        student_sid = input("Enter  SID  :")
        if student_sid.strip().isdigit():
            input_ok = True  
        else:
            print("\nSID can only be a combination of numbers!!! ")
        
    user_data[student_sid]=student_name
    str = "k"
    while(str.lower()!="y" and str.lower()!="n"):
        str=input("\nDo you want to store more student data (Y/N) : \n")
        if str.lower()=="n":
            program_flow = False
        elif str.lower()!="y" :
            print("\nPlease enter Y or N only!!!\n")
    
# a. Print students details stored in the dictionary.

print("\nStudent data in the order as entered by the user : ")
for student_sid , student_name in user_data.items() :
    print(student_sid," : ",student_name)

# b. Sort dictionary using student names.
sorted_names = sorted(user_data.values())
new_user_data ={}
for student_name in sorted_names:
    for student_sid , names in user_data.items():
        if(names==student_name):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student names :")
for student_sid ,student_name  in new_user_data.items() :
    print("{:<15}:{:<15}".format(student_sid,student_name))

# c. Sort dictionary using student sids.

sorted_sids = sorted(user_data.keys())
new_user_data ={}
for student_sids in sorted_sids:
    for student_sid , student_name in user_data.items():
        if(student_sid==student_sids):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student sids :")
for student_sid,student_name in new_user_data.items() :
    print(student_sid," : ",student_name)

# d. Search a student details with SID and print name of that student.

input_ok = False
while(input_ok == False):
    search_sid = input("\nEnter the SID whose name you want to search :")
    if search_sid.strip().isdigit():
        input_ok = True
    else:
        print("\nSID can only be a combination of numbers!!! ")

if search_sid in user_data:
    print("\nName of the student with SID {} is {}.".format(search_sid,user_data[search_sid]))
else:
    print("SID {} is not present in our data.".format(search_sid))

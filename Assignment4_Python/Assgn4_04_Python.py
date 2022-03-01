# Creating a class
class Student:
    
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        
    def __del__(self):
        print("deleeeeted")

s1=Student('Haramrit Singh', 21104055)

print(s1.name)
print(s1.rollnumber)

# calling del function to destroy object
del s1
print(s1.rollnumber)

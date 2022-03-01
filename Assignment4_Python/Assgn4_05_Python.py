#Creating a class
class Employee:
    def __init__(self,ID,Name,salary):
        self.ID=ID
        self.Name=Name
        self.salary=salary

p1=Employee('1','Mehak','40000')

print(p1.ID)
print(p1.Name)
print(p1.salary)

print()        
p2=Employee('2','Ashok','50000')

print(p2.ID)
print(p2.Name)
print(p2.salary)

print()
p3=Employee('3','Viren','60000')

print(p3.ID)
print(p3.Name)
print(p3.salary)

print('')

# Updating an argument
p1.salary=70000

print(p1.ID)
print(p1.Name)
print(p1.salary)

print()

# Deleting a record
del p3.ID
del p3.Name
del p3.salary

# By printing the three items listed below we will get an error proving that the record has been deleted
print(p3.ID)
print(p3.Name)
print(p3.salary)

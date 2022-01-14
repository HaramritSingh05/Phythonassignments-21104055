#Question 5-A Python program to print a specified list after removing 4th element.
colours=["Red","Green","White","Black","Pink","Yellow"]
print("The original list of colours is",colours)
del colours[3]
print("After deleting the colour :", colours)


#--------*************-------------

#Question 5-B Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
colours=["Red","Green","White","Black","Pink","Yellow"]
colours[3:5]=["Purple"]
print("List after replacing black and white with purple is :",colours)

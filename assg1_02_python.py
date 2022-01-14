#Python program to compute a person's income tax #
a=input(" Enter your Gross Income: ")
b=int(a)
c=10000
d=input("Enter your no. of dependents: ")
e=3000
f=int(d)
print("The taxable income of one man is :",b-c-(e*f))

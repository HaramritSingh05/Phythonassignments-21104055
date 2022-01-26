string='Python is a case sensitive Language'

#length of the input string
print(len(string))


#Reversing the order
a=string[len(string)-1::-1]
print(a)


#Slicing
b=string[10:26]
print(b)


#Use of replace function
string2=string.replace('a case sensitive','object oriented')
print(string2)


#Finding index of substring
print(string.find('a'))


#use of replace function
c=string.replace(' ','')
print(c)

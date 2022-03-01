# Calculating and printing quotient and remainder of 2 input values
num1=int(input('Enter a number here :\n'))
num2=int(input('Enter a number here :\n'))

def remainder(num1, num2):
    return num1%num2

def quotient(num1, num2):
    return num1//num2

quot = quotient(num1, num2)
rem = remainder(num1, num2)


# Using f-string
print(f'The quotient of num1 and num2 is {quot} ', ) 
print(f'The remainder when num1 is divided by num2 is {rem} ')


# (a) Checking whether the function/values are callable or not
print(callable(num1))
print(callable(remainder))


# (b) Checking whether all the values are zero or not.
num = (num1, num2)
print(all(num))


# (c) Adding values to a set 
lst=[]
lst.append(quot)
lst.append(rem)
lst.extend([4,5,6])

def function(x):
    if x>4:
        return True
    else: return False

#filtering out values with some given condition
filteredLst = list(filter(function, lst))
print("Filtered list: ", filteredLst)

# (d) Creating a set
st = set(lst)
print(st)


# (e) Making the set immutable

#empty frozenset
new_set = frozenset(st)

print("Immutable set using frozenset: ", new_set)


# (f)
def MAX(anyset):
    return max(anyset)
t=MAX(new_set)
print(t)
u = hash(t)
print(f'The integer hash value of the maximum number in the set is {u} ')



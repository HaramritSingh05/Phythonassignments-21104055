n=int(input('Enter the size of the list here: '))
lst=[]
for i in range(n):
    B=int(input(' Enter a number here: '))
    sq=B**2
    pair = (B, sq)
    lst.append(pair)
print(lst)

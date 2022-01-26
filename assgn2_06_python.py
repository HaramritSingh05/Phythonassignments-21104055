l1=int(input('Enter length of first side of triangle:\n'))
l2=int(input('Enter length of second side of triangle:\n'))
l3=int(input('Enter length of third side of triangle:\n'))
if (l1>l3+l2 or l2>l1+l3 or l3>l1+l2):
    print('No')
else:
    print('Yes')
    

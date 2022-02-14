def fibnum(n):    #n is the number in fib sequence to be printed
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibnum(n-1)+fibnum(n-2)
sum=0
n = int(input("number of numbers in sequence: "))
for i in range(n):
    fib = fibnum(i)
    print(fib)
    sum=sum+fib
average=sum/n
print('The average of the Fibonnaci sequence is : ' + str(average))



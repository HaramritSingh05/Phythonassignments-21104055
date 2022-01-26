#A python program to find the greatest of three numbers entered by the user.
Num1=int(input('Enter First Number Here:\n'))
Num2=int(input('Enter Second Number Here:\n'))
Num3=int(input('Enter Third Number Here:\n'))
# Comparison between first two numbers.
if Num1>Num2:
    if Num1>Num3:
        '''Since Num 1 is greater than Num 2, if it is greater than
Num 3 then Num3 is the highest number otherwise Num3 is the highest number'''
        print('Num1 is the Greatest Number')
    else:
        print('Num3 is the Greatest Number')
else:
    if Num2>Num3:
        print('Num2 is the Greatest Number')
    else:
        print('Num3 is the Greatest Number')
    
        

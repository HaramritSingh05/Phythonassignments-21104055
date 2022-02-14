#The Grade and the performance of a student
gradepoints=int(input('Enter the Grade Points of student: '))
if gradepoints==10:
    print('Your Grade is ‘A+’ and Outstanding Performance')
elif gradepoints==9:
    print('Your Grade is ‘A’ and Excellent Performance')    
elif gradepoints==8:
    print('Your Grade is ‘B+’ and Very Good Performance')
elif gradepoints==7:
    print('Your Grade is ‘B’ and Good Performance')
elif gradepoints==6:
    print('Your Grade is ‘C+’ and Average Performance')
elif gradepoints==5:
    print('Your Grade is ‘C’ and Below Average Performance')
elif gradepoints==4:
    print('Your Grade is ‘D’ and Poor Performance')
else:
    print('ERROR')

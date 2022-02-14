#Using String slicing and spaces to form a pattern
partialabcd='ABCDEFGHIJK'
for i in range(len(partialabcd),0,-2):
    print(' '*int((11-i)/2) + partialabcd[:i] + ' '*int((11-i)/2))
          

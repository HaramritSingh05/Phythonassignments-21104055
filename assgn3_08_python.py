Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Given sets are :")
print("Set1 = ",Set1)
print("Set2 = ",Set2)
print("Set3 = ",Set3)


#****************************************************************
# We can use |(or) operator or union method on sets to find Union.
# We can use &(and) operator or Intersection on sets to find Intersection.
# We can use -(difference )  operator  for Difference between sets.
#****************************************************************




# a. Create a new set of all elements that are in Set1 and Set2 but not both.

new_set = Set1.union(Set2) - Set1.intersection(Set2)
print("\nNew set of all elements that are in Set1 and Set2 but not both : ", new_set)

# b. Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

unique_element_set = (Set1|Set2|Set3) - (Set1 & Set2)-(Set2 & Set3) - (Set3 & Set1)
print("\nNew set of all elements that are in only one of the three sets Set1, Set2 and Set3 :",unique_element_set)

# c. Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.  

exactly_two = (Set1 & Set2)|(Set2 & Set3)|(Set3 & Set1)-(Set1 & Set2 & Set3)
print("\nNew set of elements that are exactly two of the sets Set1, Set2 and Set3 : ",exactly_two)

# d. Create a new set of all integers in the range 1 to 10 that are not in Set1.

set_in_range = set(x for x in range(1,11)) - Set1
print("\nNew set of all integers in the range 1 to 10 that are not in Set1 :", set_in_range)

# e. Create a new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.

new_set_in_range = set(x for x in range(1,11)) - (Set1|Set2|Set3)
print("\nNew set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",new_set_in_range)

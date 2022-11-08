# Task 1
#Make a list containing the names of your friends, and it contains at least 5 names
# What is required in the first and second line is to print the name of the first friend in the list in two ways,
#then in the third and fourth line you print the name of the last friend in the list in two ways

friends = ["Mazen", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])  
print(friends.pop(0))  
print(friends[-1])  
print(friends.pop(-1)) 

# Task 2
#From the previous list, print the odd names on the first line,
#  and on the second line, print the even names

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])  

print(friends[1::2]) 


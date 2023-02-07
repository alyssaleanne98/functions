#CHALLENGES

#Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_tothat(n): #function named sum_tothat accepts n
    return sum(range(1, n+1))

print(sum_tothat(6))

#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums): #function named largest 
    return max(nums) #returning max() function returns the item with the highest value
print (largest([10, 4, 2, 231, 91, 54]) ) # returns 231

#for loop and if statement

#Write a function named occurancesthat takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# look into a method 
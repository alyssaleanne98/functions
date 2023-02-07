#CHALLENGES

#Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_tothat(n): #function named sum_tothat accepts n
    return sum(range(1, n+1))

print(sum_tothat(6))

#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums): #function named largest 
    return max(nums) #returning max() function returns the item with the highest value
print (largest([10, 4, 2, 231, 91, 54]) ) # returns 231



#Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurences (string1, string2):
    return string1.count(string2) # count() method returns the number of elements with the specified value.

print(occurences('fleep floop', 'e'))

#Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
#(HINT: Review your notes on *args).

def product (*a): # * is used to pass a variable number of arguments to a function
    result = 1
    for num in a:
        result *= num # *= is Multiple AND
    return result

print(product(-1, 4))
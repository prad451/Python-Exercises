############################Python Exercises#############################

'''Exercise 1: Calculate the multiplication and sum of two numbers :
    Given two integer numbers return their product only if the product is equal to or lower than 1000, 
    else return their sum.'''

def mul_or_sum(num1,num2):
    product = num1 * num2
    if product<=1000:
        return product
    else:
        return num1 + num2
result = mul_or_sum(29,49)
print(result)





'''Exercise 2: Print the sum of the current number and the previous number:
   Write a program to iterate the first 10 numbers and in each iteration, 
   print the sum of the current and previous number.'''
   
previous_num = 0
for i in range(11):
    sum = i + previous_num
    print(f"Current number {i} Previous number {previous_num} Sum {sum}")
    previous_num = i
    
    
    
    

'''Exercise 3: Print characters from a string that are present at an even index number : Write
   a program to accept a string from the user and display characters that are present at an even index number.'''
   
mystr = input("Enter the string : ")
n = len(mystr)
for i in range(0,n-1,2):
    print(mystr[i])   #print("index[", i, "]",(mystr[i])) 
    
#or we can do using list slicing
mystr = input("Enter the string : ")
lst = list(mystr)
for i in lst[0::2]:
    print(i)
    
    
    
    

'''Exercise 4: Remove first n characters from a string : Write a program to remove characters 
    from a string starting from zero up to n and return a new string.'''

def remove_chars(str,n):
    print("Original string is : ",str)
    x = str[n:]
    return x
print(remove_chars("pradnya",5))
print(remove_chars("pradnya",3))




'''Exercise 5: Check if the first and last number of a list is the same : Write a function to return True if 
   the first and last number of a given list is same. If numbers are different then return False.'''

lst1 = [10, 20, 30, 40, 10]
lst2 = [75, 65, 35, 75, 30]
def first_last_num(number):
    first_num = number[0]
    last_num = number[-1]
    if first_num==last_num:
        return True
    else:
        return False
print("Result is : ",first_last_num(lst1))
print("Result is : ",first_last_num(lst2))




'''Exercise 6: Display numbers divisible by 5 from a list :
   Iterate the given list of numbers and print only those numbers which are divisible by 5'''

lst = [10,20,18,19,55,20]
print("This is the given list :",lst)
print("The numbers which are divisible by 5 are : ")
for i in lst:
    if i%5==0:
        print(i)
        
        
        
        

'''Exercise 7: Return the count of a given substring from a string : Write a program to find
   how many times substring “Emma” appears in the given string.'''

myStr = "Emma is good developer. Emma is a writer"   
cnt = myStr.count("Emma")
print(f"Emma is appeared {cnt} times")

#without using string method
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")





'''Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

for i in range(6):
    for j in range(i):
        print(i,end='')
    print("\n")
 
 
 
 
    
'''Exercise 9: Check Palindrome Number :Write a program to check if the given number is a palindrome number.
   A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers.'''

num = int(input("Enter the number : "))
temp = num
rev = 0

while num>0:
    remainder = num%10
    rev = rev*10+remainder
    num = num//10
if temp==rev:
    print("Given number is a palindrome!!!")
else:
    print("Given number is not a palindrome!!!")


#palindrome string
letter = "MOM"
rev = reversed(letter)
if list(letter)==list(rev):
    print("Palindrome!")
else:
    print("Not a Palindrome!")

#or
letter = input("Enter a letter : ")
if (letter==letter[::-1]):
    print("Palindrome..")





'''Exercise 10: Create a new list from a two list using the following condition : Create a new list from a two 
   list using the following condition.Given a two list of numbers, write a program to create a new list such 
   that the new list should contain odd numbers from the first list and even numbers from the second list.'''
   
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for i in list1:
    if i%2!=0:
        list3.append(i)
for i in list2:
    if i%2==0:
        list3.append(i)
print(list3)

#or
def new_list(list1,list2):
    for i in list1:
        if i%2!=0:
            list3.append(i)
    for i in list2:
        if i%2==0:
            list3.append(i)
new_list(list1,list2)
print(list3)





'''Exercise 11: Write a Program to extract each digit from an integer in the reverse order.'''

num = int(input("Enter the number : "))
while num>0:
    digit = num % 10
    num = num // 10
    print(digit,end = " ")



num = input("Enter the number : ")
for i in num:
    i=num[::-1]
print(i)





'''Exercise 12: Print multiplication table form 1 to 10'''

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\t\t")




    
'''Exercise 13: Print downward Half-Pyramid Pattern with Star (asterisk)'''

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


'''Exercise 14: Print downward full-Pyramid Pattern with Star (asterisk)'''

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")





'''Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to 
   the power of exp. : Note here exp is a non-negative integer, and the base is an integer.'''

def exponent(base, exp):
    result = base**exp
    return result
x = exponent(2,5)
print(x)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
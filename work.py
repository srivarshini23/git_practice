"""hello_str ="Hello World"
position = hello_str.find("World")
print("Position of 'World':", position)

lower_str = hello_str.lower()
upper_str = hello_str.upper()

print("Lowercase:", lower_str)
print("Uppercase:", upper_str)

# Replacing a substring
replaced_str = hello_str.replace("World", "Python")
print("Replaced String:", replaced_str)

#Splitting a string
words = hello_str.split(" ")
print("Words in the string:", words)

#formatting String 
name = "Sri varshini"
age =24
Company = "TCS"

Myself = ("Myself {} and age is {} ,Working in {}" .format(name,age,Company))
print(Myself)

Programming = 'python'
sentence = ("i am working on {}".format(Programming))
print(sentence)

d = Programming[1:6:3]
print(d)

# Iterating through each character in a string
for char in "Iteration":
    print(char,end='  ')  # Prints each character followed by a space
print() """

"""
# Joining a list of strings into a single string
words = ['Python', 'is', 'fun']
joined_str = ' '.join(words)
print(joined_str)

Sentence1 = ["myself","is","Varsha","working","on","python"]
j = "  ".join(Sentence1) 
print(j)

mystring = "This is a String"
mylist =[]
for word in mystring:
    mylist.append(word)
print(mylist)

"""
"""
for x in range(100):
    print(x)
    if x % 3 == 0:
        print("Frizz")
        continue
    else:
        print("Buzz")


mywork = [x for x in range(100) if x%5==0]
print(mywork) """
"""
s1 = ["vennalaa","sri","varsha"]
joined_str =" ".join(s1)
print(joined_str)


"""
"""
Para=" Sun is too sunny today so take sun screencream with you  "
z = Para.lower()
print(z ,end = "  ")
words = Para.split()
print(words)

for x in words:
   if x[0] == "s":
    print("words found:",x)

   


for x in range(10):
    if x % 2 == 0:
        print("It is Even number:",x)
    else:
        print("It is Odd number:",x)

Num = [x for x in range(1,50) if x%3 ==0]
print("It is divisible by 3",Num) 




t1 = "Sun is too sunny today so take sun screencream with you"
c = t1.split()
print(c)
for x in c:
    if len(x) % 2 == 0:
        print("even",x) """
"""
for i in range(100):
    
    if i % 3 == 0 and  i%5 == 0:
        
        print("FrizzBUZZ",i)
    
    elif i%5 == 0:
        print("BUzz",i)

    elif i%3 == 0:
        print("Frizz",i)
    else:
        print(" ")


"""
"""
s1 = "Sun is too sunny today so take sun screencream with you"
s2 = s1.split()
print(s2)
c = [x[0] for x in s2 ]
print(c)

"""


'''def evencheck(a,b):
    
    if  (a  % 2 == 0 and b %2 ==0 )and (a < b) :
        return f'This is the lowest of two even number :{a}'

    elif(a% 2 == 1 and b %2 == 1 )and (a > b or a == b):
        return f'This is the greater one or equal number of the odd numbers:{a}'

    elif( a %2 ==0 and b %2 != 0) and (a > b):
       return f'This is the greater one of the odd numbers:{a}'
    elif( a %2 ==0 and b %2 != 0) and (a < b):
       return f'This is the greater one of the odd numbers:{b}'
    elif( a %2 !=0 and b %2 != 0) and (a < b):
       return f'This is the greater one of the odd numbers:{a}'
       
    
res = evencheck(5,1)
print(res)




def string1(name):
    a = name.split()
    print(a)
    #for i,b in enumerate(a):
        #print(i,b)
    c= a[0]
    d= a[1]
    if c[0] == d[0] :
        print("both matches")
        return True
    else :
        print("Not matched")
        return False
            
    
word = string1("varsha Varshini")
print(word) '''

'''
def seven_value(num):
    
    num =num+7

    return num

print(seven_value(6)) '''

'''

def captial_of_1st_and_4th_letter(word):
    #we have make the first and fourth letter to capital with our code
    first_letter = print(word[0].upper())
    fourth_letter =print(word[3].upper())
    return word

print(captial_of_1st_and_4th_letter('varshini')) '''

'''
def sentence(anystring):
    # Split the string into words
    words = anystring.split()
    # Reverse the list of words
    words.reverse()
    # Join the reversed list back into a string
    reversed_sentence = ' '.join(words)
    # Return the reversed sentence
    return reversed_sentence

# Test the function
print(sentence("i am in office")) '''

"""
#Write a function that gives the volume of the sphere 

def radius(r):
    x = (4/3)*(22/7)*(r**3)
    return x

print(radius(4))"""
'''
#write a function and check if the given number is in the given range of numbers

List1 = range (100)
def func():
    for x in List1:
        x=x+1
        if x < 100 or x == 100:
            print ("Number is within the range")
        else:
            print("Number is out of the range")
        return x

print(func())'''
'''
# Original string to get the count of the capital and small letter in a string
string1 = "Myself Sri Varshini Sakkuri from TCS Cisco"

def count_letters(text):
    capital_count = 0
    small_count = 0
    for char in text:
        if char.isupper():
            capital_count += 1
        elif char.islower():
            small_count += 1
    return capital_count, small_count

# Call the function and print the result
capital_count, small_count = count_letters(string1)
print(f"Capital letters count: {capital_count}")
print(f"Small letters count: {small_count}")
'''
'''
#write a function to get the list of unqiue values from the list and return new list

List1 = [1,1,1,2,2,2,23,3,3,4,4,4,4,46,6,6,55,4,4,43,3,5,5,6,6,7,8,9,7]
def new_list():
    list2 = set(List1)
    print(list2)
    newlist = list((list2))
    return newlist

print(new_list())

'''
'''
def user_choice():
    choice_name = str(input("Enter your name: "))
    while True:
        age = input("Enter age: ")
        if age.isdigit():
            age = int(age)
            if 18 <= age <= 25:
                break
            else:
                print("Enter the correct age. You must be between 18 and 25 years old.")
        else:
            print("Please enter a valid number for your age.")
    
    company = input("Enter your company: ")
    print(choice_name, age, company)

# Call the function and print the result if needed


print(user_choice())

'''
'''
#Reversing a string
str1 = "Varsha"
str1 = str1[::-1]
length_str1 = len(str1)
print("Here is the reverese String :",str1)
print("length of the String : " ,length_str1)

for index,letter in enumerate(str1):
    print(f'Index of the letter:{index}\n Letter of the word : {letter}')


def index_value():
    str2 = "sri varshini"
    str3 = list(str2)
    print(len(str3))
    return str3

print(index_value()) '''

"""def game():
    print("Below are the positions available please select one :")
    row1 = ['a ','b ', ' c']
    row2 = ['',' ', ' ']
    row3 = [' ',' ', ' ']
    print(row1)
    print(row2)
    print(row3)
    Choose_a_position = input("Enter the postion you wanna index value:")
    if row1[0] == Choose_a_position:
    
        
            row1 = input("Enter your choice :  ")
            row1[0].replace('a',{row1})
            print(row1)
        #elif row[1] == 'b':
            row1 == input ("Enter your choice : ")
            print(row1)
        #elif i == Choose_a_position:
            row1 == input("Enter your choice: ")
            print(row1)

print(game())"""

'''
text = " This is ****** and working on python along with ******"

text1 = text.split()
Your_choice = input('enter index number :')
print(Your_choice)

def fn():
    flag = 0
    for index,i in enumerate(text1):
        print(index,i)
        # print(type(Your_choice),type(index))
        if int(Your_choice) == index:
            flag = index
            # print("Test")
    print("Matching" + text1[flag])


fn()

'''

"""from random import shuffle
list1 = [1,2,3,4,5,6,7,8,9]
shuffle(list1)
print(list1)"""
'''
import random
list1 = [1,2,3,4,5,6,7,8,9]
random.shuffle(list1)
print(list1)

'''
'''
#Write a function to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become 
# smaller than the original string, your function should return the original string.   
        
def compress_string(s):
    # Initialize the compressed parts list and counters
    compressed_parts = []
    count_consecutive = 0
    
    # Iterate through the string, counting consecutive characters
    for i in range(len(s)):
        count_consecutive += 1
        # If next char is different than current, append this char to result
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed_parts.append(s[i] + str(count_consecutive))
            count_consecutive = 0  # Reset the counter
    
    # Combine the parts into the compressed form
    compressed = ''.join(compressed_parts)
    # Check if the compressed string is shorter than the original
    return compressed if len(compressed) < len(s) else s

# Example usage:
original_string = "aabcccccaaa"
print(compress_string(original_string))  # Output: a2b1c5a3

'''    
'''
#Length of Last Word: Given a string consisting of upper/lower-case alphabets and empty space characters ' ',
#  return the length of the last word in the string. If the last word does not exist, return 0.
             
Sentence = "varsha "

New_list = Sentence.split()
print(New_list)

if Sentence.islower() or Sentence.isupper()  or Sentence.isspace():
    Lastword = len(New_list[-1])
    print(Lastword)
else:
    print("Lastword doesn't exit or 0" )

=====================================================================

count = 0
a = [ ]
for i in range(9):
    count = count+i
    a.append(count)
    print(count)
    
print(a)



L1 = 'aabccadb'
j = list((L1))
print((j))
L2 = [ ]
for i in range(len(j)):
    if i == len(j) - 1 or j[i] != j[i+1] :
        L2.append(j[i])
    else:
        pass
print(L2)
        
'''
   
def myfunc(*args):
    a = []
    for i in args:
        if i%2 ==0  :
            a.append(i)
            print(f'even number :{i}')
    else:
        pass
        
myfunc(1,2,3,4)
    
        






















 










   

        


    
    

   
    
    



    
    







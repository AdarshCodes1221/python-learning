'''fruits =["orange" , "aplle" , "Mango"] #This is list in python 
x,y,z = fruits #Unpacking the list 
print(x)
print(y)
print(z)
------------------------------------------------------------------------------------
 fruits={"orange", "apple" , "Mango"} #This is set in python
x,y,z = fruits #Unpacking the set   
print(x)
print(y)        
print(z)

------------------------------------------------------------------------------------
x = "awesome" #Global variable
def myfunc():
    print("python is " + x)#Using the global variable inside the function
myfunc()
------------------------------------------------------------------------------------
# Type Conversion in python
a=1.60
b=2
c=1j

d=int(a) #Converting float to integer
e=float(b) #Converting integer to float
f=complex(b) #Converting integer to complex
#e=int(c) #Converting complex to integer (will raise an error)
print(d)
print(e)    
print(f)

------------------------------------------------------------------------------------

# Random Number Generation in python
import random   
print(random.randint(1,10)) #Generates a random integer between 1 and 10 (inclusive

------------------------------------------------------------------------------------
#Python Casting  ( important    )
#Specify a Variable Type
#There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

#Casting in python is therefore done using constructor functions:

#int() - constructs an integer number from an integer literal, 
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)
------------------------------------------------------------------------------------
#Python 
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
a = "Hello"
print(a)

Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
b = 'Hello'
print(b)
------------------------------------------------------------------------------------
Multiline Strings

You can assign a multiline string to a variable by using three quotes:
c = """This is a 
multiline string."""    
------------------------------------------------------------------------------------
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string. 
a = "Hello, World!"
print(a[3])
------------------------------------------------------------------------------------
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Adarsh Jha":
  print(x)

------------------------------------------------------------------------------------
String Length
To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))
------------------------------------------------------------------------------------
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in. 
txt = "The best things in life are free!"   
print("free" in txt)    
print("expensive" in txt)

------------------------------------------------------------------------------------
Python - Slicing Strings
Slicing
You can return a range of characters by using the slice syntax. 
b = "Hello, World!"
print(b[2:9])   
#This will print the characters from position 2 to position 8 (9 is not included)
------------------------------------------------------------------------------------
Slice From the Start
By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])    
------------------------------------------------------------------------------------
Slice To the End        
By leaving out the end index, the range will go to the end of the string: 
b = "Hello, World!" 
print(b[2:])

------------------------------------------------------------------------------------
Negative slicing
Use negative indexes to start the slice from the end of the string: 
b = "Hello, World!"
print(b[-5:-2]) #This will print the characters from position -5 to position -3 (the character at position -2 is not included)
------------------------------------------------------------------------------------
Ab negative indexing kya hoti hai?
👉 Negative indexing ka matlab hai ginti RIGHT se (end se) shuru karna
 H   e   l   l   o   ,       W   o   r   l   d   !
-13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

----------------------------------------------------------------------------
*Python - Modify Strings
Modify Strings
Python has a set of built-in methods that you can use to modify strings.
#upper() Method
The upper() method returns the string in upper case:    
a = "Hello, World!"
print(a.upper())    

#lower() Method
The lower() method returns the string in lower case:    
a = "Hello, World!"
print(a.lower())

#strip() Method
The strip() method removes any whitespace from the beginning or the end: 
a = "                   Hello, World!  "       
print(a.strip()) # returns "Hello, World!"

#replace() Method
The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#split() Method
The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
 
------------------------------------------------------------------------------------

#First day at learning python

--------------------------------
Python - String Concatenation
String Concatenation
To concatenate, or combine, two strings you can use the + operator. 
a = "Hello"
b = "World" 
c = a + b
print(c)
------------------------------------  
Python - Format - Strings
Format Strings
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age  #This will raise an error
print(txt)

F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"  
print(txt)

------------------------------------------------------------------------------------
#Python - String Methods
String Methods
Python has a set of built-in methods that you can use on strings.
#capitalize() Method
The capitalize() method converts the first character to upper case: 
a = "hello, and welcome to my world."
print(a.capitalize())
#count() Method
The count() method returns the number of times a specified value occurs in a string:
a = "Hello, welcome to my world."
print(a.count("o"))
#endswith() Method
The endswith() method returns True if the string ends with the specified value: 
a = "Hello, welcome to my world." 
print(a.endswith("."))
#find() Method
The find() method finds the first occurrence of the specified value:
a = "Hello, welcome to my world."
print(a.find("welcome"))
#join() Method
The join() method takes all items in an iterable and joins them into one string.  A string must be specified as the separator.
myTuple = ("John", "Peter", "Vicky")  
x = "#".join(myTuple)
print(x)
 
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

------------------------------------------------------------------------------------
*Escape Character
 To insert characters that are illegal in a string, use an escape character.

 An escape character is a backslash \ followed by the character you want to insert.

 An example of an illegal character is a double quote inside a string that is surrounded by double quotes: 
 txt = "We are the so-called \"Vikings\" from the north."
 print(txt)

------------------------------------------------------------------------------------
* Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)   #True
print(10 == 9)  #False
print(10 < 9)   #False
------------------------------------------------------------------------------------
#Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return 
print(bool("Hello"))  #True
print(bool(15))       #True
print(bool(""))      #False
print(bool(0))      #False #Zero is considered as False
print(bool(None))   #False #None is considered as False
print(bool([]))     #False #Empty list is considered as False
print(bool({}))     #False #Empty dictionary is considered as False
print(bool(set()))  #False #Empty set is considered as False
print(bool(()))     #False #Empty tuple is considered as False
------------------------------------------------------------------------------------

#Functions that Return a Boolean
The following functions return a boolean value:   
* isinstance() - Returns True if a specified object is of the specified data type
* issubclass() - Returns True if a specified class is a subclass of a specified object
#Example
x = 200
print(isinstance(x, int))  #True

#example
class Person:
  pass
class Student(Person):
  pass
print(issubclass(Student, Person))  #True

------------------------------------------------------------------------------------
Python Operators
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups: 
* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators
------------------------------------------------------------------------------------
#Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:
Operator	Description	Example
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y
------------------------------------------------------------------------------------
#Assignment Operators
Assignment operators are used to assign values to variables:
Operator	Description	Example
=	Assigns values	x = 5
+=	Adds and assigns	x += 3
-=	Subtracts and assigns	x -= 3
*=	Multiplies and assigns	x *= 3
/=	Divides and assigns	x /= 3
%=	Modulus and assigns	x %= 3
**=	Exponentiation and assigns	x **= 3
//=	Floor division and assigns	x //= 3
------------------------------------------------------------------------------------
#Comparison Operators
Comparison operators are used to compare two values:
Operator	Description	Example
==	Equal	x == y
!=	Not equal	x != y
>	Greater than	x > y
<	Less than	x < y
>=	Greater than or equal to	x >= y
<=	Less than or equal to	x <= y
------------------------------------------------------------------------------------
#Logical Operators
Logical operators are used to combine conditional statements:
Operator	Description	Example
and	Returns True if both statements are true	x < 5 and  x < 10
or	Returns True if one of the statements is true	x < 5 or x < 40
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
#code example
x = 5
print(x > 3 and x < 10)  #True
print(x > 3 or x < 4)    #True
print(not(x > 3 and x < 10))  #False

-----------------------------------------------------------------------------------
#Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Operator	Description	Example 
is	Returns True if both variables are the same object	x is y
is not	Returns True if both variables are not the same object	x is not y  
#code example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)      #True
print(x is y)      #False 
print(x is not y)  #True
------------------------------------------------------------------------------------
#Membership Operators
Membership operators are used to test if a sequence is presented in an object:
Operator	Description	Example
in	Returns True if a sequence with the specified value is present in the object	x in y
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
#code example
x = ["apple", "banana"]
print("banana" in x)      #True
print("pineapple" not in x)  #True
------------------------------------------------------------------------------------
#Bitwise Operators
Bitwise operators are used to compare (binary) numbers:
Operator	Description	Example
&	AND	Sets each bit to 1 if both bits are 1  x & y
|	OR	Sets each bit to 1 if one of two bits is 1  x | y
^	XOR	Sets each bit to 1 if only one of two bits is 1  x ^ y
~	NOT	Inverts all the bits  ~x    
<<	Zero fill left shift  Shift left by pushing zeros in from the right and let the leftmost bits fall off  x << 2
>>	Signed right shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off  x >> 2
#code example
x = 10  #Binary: 1010 
y = 4   #Binary: 0100
print(x & y)  #Output: 0  (Binary: 0000)
print(x | y)  #Output: 14 (Binary: 1110)
print(x ^ y)  #Output: 14 (Binary: 1110)  
print(~x)     #Output: -11 (Binary: ...11110101)
print(x << 2) #Output: 40 (Binary: 101000)

******The Walrus Operator
Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

ExampleGet your own Python Server 
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

-------------------------------------------------------------------------------------
#****Operator Precedence
Operator precedence describes the order in which operations are performed.

Operator	Description	Example
()	Parentheses (highest precedence)	(2 + 3) * 5 
**	Exponentiation	2 ** 3 # what is 2 to the power of 3 #?
+x, -x	Unary plus and minus	-x  
*, /, //, %	Multiplication, division, floor division, modulus	10 * 5
+, -	Addition and subtraction	10 + 5  
<<, >>	Bitwise shift operators	x << 2
&	Bitwise AND	x & y
^	Bitwise XOR	x ^ y
|	Bitwise OR	x | y
#code example
x = 10 + 3 * 2 ** 2
print(x)  #Output: 22
-----------------------------------------------------------------------------------


'''
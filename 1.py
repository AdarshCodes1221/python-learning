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




'''
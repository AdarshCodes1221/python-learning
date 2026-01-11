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
'''

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

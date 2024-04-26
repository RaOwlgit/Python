#Type casting - It is the process of converting one data type into andother data type
#Python supports a wide varity of function or method like:int(),float(),str(),ord()
#hex(),oct(),tuple()set(),list(),dict() ect

#Explecti TypeCasting

string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print("The sum of both the number is :",sum)

#Implecit TypeCasting

num1 = 1.9 #which is a float datatype
num2 = 8 #which is an intiger
sum = num1 + num2
print(type(sum),end = "-")
print(sum)

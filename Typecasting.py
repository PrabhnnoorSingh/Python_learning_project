#Type casting

name = "Prabhnoor "
age = 20
gpa = 3.2
is_student = True

#using typecasting
age = float(age)
print(age)
gpa = int(gpa)
age = str(age)
#doesn't work
#age += 1
age += "1"
print(age)
print(gpa)

#If we turn the name into a boolean it will tell us if the string is empty or not 
name = bool(name)
print (name)
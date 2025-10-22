studentInfo= {
    100 : "Tamim khan",
    101 : "Hannan khan",
    103 : "Mannan khan",
    104 : "Tahmina begum",
}
print(studentInfo.get(104 , "Default value doesn't exits"))


# how to decleare tuple and print the tuple value

studentInfo = (
    ("Anisul Islam", 27, 3.56, "Khaidza"),
    "Rabeya begumn",
    "Tamim khan",
)

# tuple doesn't support key value changed
print(studentInfo[0:])

# how to set work and also decleare a set
num1 =  {1,2,3,4,5}
num2 = set([4,5,6])

# added a value into the set
num2.add(10)
num2.remove(4)
print(num2)
# also check is else statement into the set value
# print(4 not in num2)
# how to print union value between the num1 and num2
print("\n")
print(num1 | num2)
print(num1 & num2)
print(num1 ^ num2)
print(num1 - num2)
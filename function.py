
def add(a, b):
    sum = a+b
    print(sum)

def default():
    print("Default function! Hello world")
add(1,2)
default()


def max_val(a, b,c):
    return max(a, max(b,c))
res = max_val(15, 90, 55)
print(res)

# how to print xxarge
# aita basically tuples ar moto kaj kore and  tuples ar moto print kore

def studentInfo(*defails):
    print(defails)
studentInfo(101, "Tamim khan")
studentInfo(104, "Tamim khan", 3.56)


# taken list and print it also akek somoy akek bar parameter ney

# def add(*num):
#     print(num)

def add(*num):
    sum2 =0
    for x in num:
        sum2 += x
    print(sum2)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50)


# xxargs, value gula key value ney,and funciton a ney ** diye and print korar jonno same way.
def student(**defails):
    print(defails)



student(id = 101, name= "Tamim khan", gpa = 3.56)



# how to use lambda function and print the value
# first a= 2 and b = 3 cole asbe and final result ta res variable ar modde cole asbe
res = (lambda a,b : a*a + 2*a*b +  b*b)(2,3)
print(res)

# how to use map function and print the value in the map
# map function take 2 type of varibale first a function others is take list

def square(x):
    return x*x
# take a value and return the square value of the taken value
num = [1,2,3,4,5]

res = list(map(square, num))
print(res)


# how to filter list value base on the condition

num = [1,2,3,4,5]
# filtering basically number gulake condition based kore pele, mane holo jei gula condition match korbe na oi value gula bad list theke
res = list(filter(lambda x: x%2==0, num))
print(res)


# zip function
# zip function basically serial wise value gula ke index base kore pele and then sob gulake zip kore pele

roll = [101, 102, 103, 104, 105,  106]
name = ["Tamim khan", "Hannan khan", "Mannan khan", "Tahmina begum", "Nasrin Akter", "Salma Akter"]
section = "ABABAAABB"

# zip basically sob gula ke ak kore niye pele and akta file ar modde sob gulake niye ase
print(list(zip(roll, name, section)))
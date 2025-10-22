# how to print list value

sub = ["C","C++", "Java", "Python", "Android", "OS", "TOC"]
print(sub)
print(sub[2])
print(sub[2:4])
print(sub[3:])
# how to print list reverse index value
print(sub[-1])
# IN or not IN print kore kivabe seta dekhbo, and seta basically true or false return kore
# python is a case sensitive language
print("android" in sub)
print("android" not in sub)

# added value into the list
print(sub + ["swift", "Go"])
# list prints 4 times or n times
print(sub * 4)
print("List length is : " ,len(sub))
# append funciton use on string, when i use append funciton on the string, it's added value in the backside

sub.append("ABC")
print(sub)

# how to use insert function in the list
sub.insert(2, "secondIndex")
print(sub)

# how to  remove a value from the list

sub.remove("TOC")
print(sub)

# how to sort list value
sub.sort()
print(sub)

arr = [10, 50, 4, 80, 33,  80, 53, 46, 80]
arr.sort()
print(arr)
arr.reverse()
print(arr)
# use pop function. It's deleted last value from the list
arr.pop()
print(arr)

new_arr = arr.copy()
# clear function deleted all value from the list
new_arr.clear()
print(new_arr)
print(arr)

# how to print index a value from the list
pos = arr.index(80)
print(pos)

# count function is count a value occurances, that's the value how many times occur

cnt = arr.count(80)
print(cnt)

# how to print a range value, that is 0 to range define value
range_vale = list(range(10))
print(range_vale)

rang_val = list(range(10, 50))
print(rang_val)
# range_val 15 index which value store, i seen it, that's why print the value
print(rang_val[15])
# mention the starting value and closing value and also mention the distance value
val = list(range(2, 100, 2))
print(val)

# how to use for loop in the list and also print the list value

for x in arr:
    print(x)
print("Loop ends")


# how to print a series

n = int(input("Enter the nth value: "))
sum1 =0
for x in range(1, n+1, 1):
    sum1 += x
print(sum1)


# list input from user and work them

arr = input("Enter a text of numbers: ")
# split diye bascially string value gulake alada alada define kore
list_val = arr.split()
sum1 = 0
for num in list_val:
    sum1 += int(num)
print(sum1)

text = input("Enter a text of numbers: ")
cnt_chr =0
cnt_digit=0
cnt_word =0
for x in text:
    x = x.lower()
    if x>='a' and x<='z':
        cnt_chr = cnt_chr + 1
    elif x>='0' and x<='9':
        cnt_digit = cnt_digit + 1
    elif x== " ":
        cnt_word = cnt_word + 1
print("number of char is :", cnt_chr, "number of digit is :- ",cnt_digit, "number of word is: -",  cnt_word+1)


import random

# n =  int(input("Enter the nth value: "))
# for i in range(n+1):
#     print(i*"*")
# for i in range(n + 1):
#     print((i*2-1) * "*")
# print("patten completed")


# create a guss number game



while True:
    guss_num = int(input("Enter the guess number between 1 and 100: "))
    rand_num = random.randint(1, 100)
    if guss_num == rand_num:
        print("Yes! You have won the game")
        break
    else:
        print("No! You have lost the game")
        print(rand_num)




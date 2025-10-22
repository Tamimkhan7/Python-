from collections import  deque

books = []

books.append("Java")
books.append("python")
books.append("c++")
print(books)
books.pop()
print(books)

books.pop()
print(books)

books.pop()
if not books:
    print("No books left")
else :
    print(books)



#queue

bank = deque(["Tamim", "Hamim", "Rasel"])
print(bank)
bank.popleft()
print(bank)

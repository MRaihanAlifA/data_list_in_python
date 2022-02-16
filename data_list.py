book_list = ['mathematics', 'science', 'chemics', 'english']

print('show all books')

for book in book_list:
    print(book)

print('show all books with len')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [12, 'science', 10, 'english']

print('\nshow new book list')

for book in book_list:
    print(book)

book_list = ['mathematics', 'science', 'chemics', 'english']
book_list.append('sociology')

print('\nshow new book list')
for i in range(0, len(book_list)):
    print(book_list[i])

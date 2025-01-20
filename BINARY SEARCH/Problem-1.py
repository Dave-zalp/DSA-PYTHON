# 1. Book Index Search
# A library database contains a sorted list of book IDs. Write an algorithm to find the position of a specific book ID in the list.
# If the book ID is not found, return an appropriate message.


class Book:
    def __init__(self, book, book_id):
        self.book = book
        self.book_id = book_id

    def locate_book(self):
        position = 0

        while position < len(self.book):

            if self.book[position] == self.book_id:
                return f'Book Found at index position {position}'

            position += 1

        return 'Book not found'


my_book = Book([1, 2, 3, 5, 7, 8, 13, 15, 19], 19)
print(my_book.locate_book())

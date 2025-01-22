# 1. Book Index Search
# A library database contains a sorted list of book IDs. Write an algorithm to find the position of a specific book ID in the list.
# If the book ID is not found, return an appropriate message.


class Book:
    def __init__(self, book, book_id: int):
        self.book = book
        self.book_id = book_id

    def locate_book(self):
        position, length = 0, len(self.book) - 1

        while position <= length:
            mid = (position + length) // 2

            if self.book[mid] < self.book_id:
                position = mid + 1

            elif self.book[mid] > self.book_id:
                length = mid - 1
            else:
                return mid

        return 'Book not found'


my_book = Book([1, 2, 3, 5, 7, 8, 13, 15, 19], 7)
print(my_book.locate_book())

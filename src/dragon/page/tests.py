from django.test import TestCase

from .models import Item, Book

# Create your tests here.

class ItemTests(TestCase):

    def test_books_should_say_they_are_a_book(self):
        non_book_item = Item()
        book_item = Book()
        self.assertIs(book_item.is_a_book(), True)
        self.assertIs(non_book_item.is_a_book, False)

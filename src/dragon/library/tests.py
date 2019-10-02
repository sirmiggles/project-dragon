from django.test import TestCase
from django.test.client import RequestFactory

# Create your tests here.

from .views import add_book
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def adding_a_book_with_no_title_should_fail(self):
        """
        It should not be possible to add a book without a title
        so attempting to do so should fail and report the error, as the
        view currently doesn't have any introspection it should be refactored
        to be made more testable before this test can evaluate it

        todo: make view testable and complete test
        """
        request = self.factory.post('library/add_book', data={'name':''})
        response = add_book(request)

    def test_is_avaliable_method_on_book(self):
        # The fields for available will be removed so in the future
        # this test will need to borrow the book to become unavailable
        available_book = Book(name='avaliable', available=True)
        unavailable_book = Book(name='unavaliable', available=False)

        self.assertTrue(available_book.is_available())
        self.assertFalse(unavailable_book.is_available())

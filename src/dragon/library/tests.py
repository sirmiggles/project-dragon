from django.test import TestCase
from django.test.client import RequestFactory

# Create your tests here.

from . import views, views_library
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_is_available_method_on_book(self):
        # The fields for available will be removed so in the future
        # this test will need to borrow the book to become unavailable
        available_book = Book(name='available')
        unavailable_book = Book(name='unavailable')
        available_book.save()
        unavailable_book.save()

        unavailable_book.borrow_item()

        self.assertTrue(available_book.is_available())
        self.assertFalse(unavailable_book.is_available())
        unavailable_book.delete(keep_parents=False)
        available_book.delete(keep_parents=False)


class RenderingViewTests(TestCase):
    """
    run views that render a page to see if they still work
    """

    def setUp(self):
        self.factory = RequestFactory()

    def assertViewWorks(self, view, start):
        try:
            request = self.factory.get(start)
            response = view(request)
            self.assertEqual(response.status_code, 200)
        except:
            self.fail()

    def test_render_library(self):
        view = views_library.ItemList.as_view()
        self.assertViewWorks(view, 'library/')

    def test_render_books(self):
        view = views.book_view
        self.assertViewWorks(view, 'library/')

    def test_render_game_view(self):
        view = views.game_view
        self.assertViewWorks(view, 'library/')

    def test_render_cardgame(self):
        view = views.cardgame_view
        self.assertViewWorks(view, 'library/')

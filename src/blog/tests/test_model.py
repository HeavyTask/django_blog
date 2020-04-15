from django.test import TestCase

from blog.models import Entry, Comment


class EntryModelTest(TestCase):

    def test_string_representaion(self):
        """
        Test string representation of entry model objects
        """
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)
    
    def test_verbose_name_plural(self):
        """
        Test verbose name plural of Entry model is Entries
        """
        self.assertEqual(str(Entry._meta.verbose_name_plural), "Entries")


class CommentModelTest(TestCase):
    def test_string_representaion(self):
        """
        Test string representation of comment model objects
        """
        comment = Comment(body="comment body")
        self.assertEqual(str(comment), "comment body")

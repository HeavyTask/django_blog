from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Entry, Comment
from blog.forms import CommentForm


class CommentFormTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testuser12345"
        )
        self.entry = Entry.objects.create(
            author=user,
            title="Entry Title",
            body="Entry Body"
        )
    
    def test_init(self):
        """
        Ensure initialization of form
        """
        CommentForm(entry=self.entry)


    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
            CommentForm()

    def test_valid_data(self):
        form = CommentForm({
            'name': "John Doe",
            "email": "jdoe@gmail.com",
            "body": "Test Comment"
        }, entry=self.entry)

        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.name, "John Doe")
        self.assertEqual(comment.email, "jdoe@gmail.com")
        self.assertEqual(comment.body, "Test Comment")
        self.assertEqual(comment.entry, self.entry)

    def test_blank_data(self):
        form = CommentForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'email': ['This field is required.'],
            'body': ['This field is required.']
        })

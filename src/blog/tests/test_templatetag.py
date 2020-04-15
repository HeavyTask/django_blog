from django.test import TestCase
from django.template import Template, Context
from django.contrib.auth import get_user_model

from blog.models import Entry

class EntryHistoryTagTest(TestCase):

    TEMPLATE = Template("{% load blog_tags %} {% entry_history %}")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="test12354"
        )

    def test_entry_shows_up(self):
        entry = Entry.objects.create(
            author=self.user,
            title="Entry Title",
            body="Entry Body"
        )
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(entry.title, rendered)

    def test_no_posts(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn('No recent entries.', rendered)

    def test_many_entries(self):
        for n in range(6):
            Entry.objects.create(
                author=self.user,
                title="Post #{0}".format(n),
            )
        rendered =  self.TEMPLATE.render(Context({}))
        self.assertIn("Post #5",  rendered)
        self.assertNotIn("Post #6", rendered)

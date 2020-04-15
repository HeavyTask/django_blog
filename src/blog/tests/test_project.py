from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Entry


class ProjectTest(TestCase):

    def test_homepage(self):
        """
        Test that homepage is working
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):
    """
    Test whether our blog entries show up on the homepage
    """
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser', password="test12345"
        )

    def test_one_entry(self):
        Entry.objects.create(title="first title", body="first body", author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'first title')
        self.assertContains(response, 'first body')

    def test_two_entry(self):
        Entry.objects.create(title="first title", body="first body", author=self.user)
        Entry.objects.create(title="second title", body="second body", author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'first title')
        self.assertContains(response, 'first body')
        self.assertContains(response, 'second title')
        self.assertContains(response, 'second body')

    def test_no_entries(self):
        response = self.client.get('/')
        self.assertContains(response, 'No blog entries yet.')



class EntryViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser', password="test12345"
        )
        self.entry = Entry.objects.create(
            title="first title", body="first body", author=self.user
        )

    def test_get_absolute_url(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        
    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)

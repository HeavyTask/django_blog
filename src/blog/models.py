from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Entry(models.Model):
    """
    Entry Model for blog post
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"


class Comment(models.Model):
    """
    Comment model for blog post
    """
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body

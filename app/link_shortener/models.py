from django.db import models
import string
import random


class LinkShortener(models.Model):
    full_link = models.TextField(unique=True, null=False, blank=False)
    hash = models.TextField(unique=True, null=False, blank=False)

    def link_shortener(self):
        """Create a random string to create a shorter link"""
        N = 7
        s = string.ascii_uppercase + string.ascii_lowercase + string.digits

        while True:
            new_shorter_link = ''.join(random.choices(s, k=N))

            if not LinkShortener.objects.filter(
                    hash=new_shorter_link).exists():
                break

        return new_shorter_link

    def save(self, *args, **kwargs):
        self.hash = self.link_shortener()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_link

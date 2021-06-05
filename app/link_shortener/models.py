from django.db import models


class LinkShortener(models.Model):
    full_link = models.TextField()
    hash_link = models.TextField(unique=True)

    def __str__(self):
        return self.full_link

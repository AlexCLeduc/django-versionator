from django.conf import settings
from django.db import models
from django.utils import timezone

from .dataloaders import BookNameLoader
from versionator import VersionModel


class CustomVersionModel(VersionModel):
    class Meta:
        abstract = True
        ordering = ["timestamp"]
        get_latest_by = "timestamp"

    timestamp = models.DateTimeField(
        default=timezone.now,
        verbose_name="hypothetical last edit date",
    )


class CustomVersionModelWithEditor(CustomVersionModel):
    class Meta(CustomVersionModel.Meta):
        abstract = True

    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

        

class AuthorVersion(CustomVersionModel):
    live_model = Author


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Book(models.Model):

    # changelog_live_name_loader_class = BookNameLoader

    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag)

    changelog_live_name_loader_class = BookNameLoader


class BookVersion(CustomVersionModelWithEditor):
    live_model = Book

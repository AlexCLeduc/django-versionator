import random

from django.contrib.auth import get_user_model
from django.db import transaction

from sample_app.data_factories import AuthorFactory, BookFactory, TagFactory
from sample_app.models import Author, Book, Tag


@transaction.atomic
def run():
    User = get_user_model()
    admin = User.objects.create_superuser(username="admin", password="admin")
    users = [User.objects.create_user(username=f"user_{i}") for i in range(10)]

    tags = list(TagFactory.create_batch(20))
    authors = [*AuthorFactory.create_batch(25), None]
    BookFactory.create_batch(200)

    for book in Book.objects.all():
        tags = random.sample(tags, 3)
        book.tags.set(tags)

    for book in Book.objects.all():
        tags = random.sample(tags, 3)
        book.author = random.choice(authors)
        book.tags.set(tags)
        book.save()
        last_ver = book.versions.last()
        last_ver.edited_by_id = random.choice(users).id
        last_ver.save()

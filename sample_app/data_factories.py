import random

import factory

from .models import Author, Book, Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("color")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("bs")
    author = factory.SubFactory(AuthorFactory)
    csv_tags = factory.LazyFunction(
        lambda: ",".join(
            factory.Faker("words", nb=random.choice([0, 1, 2, 3, 4])).generate(
                {}
            )
        )
    )

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted is not None:
            # A list of tags were passed in, use them
            self.tags.add(*extracted)

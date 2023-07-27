from pleasant_promises.dataloader import SingletonDataLoader

class BookNameLoader(SingletonDataLoader):
    @staticmethod
    def batch_load(book_ids):
        from .models import Book
        books = Book.objects.filter(id__in=book_ids).prefetch_related("author")
        by_id = {b.id: b for b in books}

        name_for_metric = lambda x: f"{x.title} ({x.author.first_name} {x.author.last_name})"
        return [name_for_metric(by_id[b_id]) for b_id in book_ids]


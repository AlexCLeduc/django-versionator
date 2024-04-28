from data_fetcher import DataFetcher


class BookNameFetcher(DataFetcher):
    @staticmethod
    def batch_load(book_ids):
        from .models import Book

        books = Book.objects.filter(id__in=book_ids).prefetch_related("author")
        by_id = {b.id: b for b in books}

        def name_for_metric(book):
            if not book:
                return ""
            if not book.author:
                return book.title

            return f"{book.title} ({book.author.first_name} {book.author.last_name})"

        return [name_for_metric(by_id[b_id]) for b_id in book_ids]

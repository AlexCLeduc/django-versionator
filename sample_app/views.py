from django.http.response import HttpResponse
from django.shortcuts import render

from data_fetcher.global_request_context import GlobalRequest

from versionator.changelog.changelog import Changelog, ChangelogConfig
from versionator.changelog.views import AbstractChangelogView

from .models import Book


def edit_book(request, pk=None):
    book = Book.objects.get(pk=pk)
    if request.POST:
        new_name = request.POST["title"]
        book.title = new_name
        book.save()

    return HttpResponse()


def changelog(request):
    """
    For now, this is just a dummy view so we can use the toolbar to see queries
    """
    page_num = int(request.GET.get("page_num", 1))

    config = ChangelogConfig(
        models=[Book],
        page_size=50,
    )

    # changelog = create_simple_changelog(
    #     models=[Book],
    #     page_size=50,
    # )
    with GlobalRequest():
        entries = Changelog(config).get_entries(page_num)
        return render(request, "changelog.html", {"entries": entries})


class ChangelogView(AbstractChangelogView):
    template_name = "changelog.html"

    def get_changelog_config(self):
        return ChangelogConfig(
            models=[Book],
            page_size=50,
        )

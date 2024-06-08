from django.urls import reverse

from sample_app.data_factories import BookFactory


def test_sample_app_view(client):

    BookFactory.create_batch(100)
    for b in BookFactory.create_batch(50):
        b.reset_version_attrs()
        b.title = "new title"
        b.save()

    url = reverse("changelog")
    response = client.get(url)
    assert response.status_code == 200

    assert len(response.context["entries"]) == 50

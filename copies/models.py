from django.db import models


class Copy(models.Model):
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )
    is_deleted = models.BooleanField(default=False)

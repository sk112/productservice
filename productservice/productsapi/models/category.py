from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=20, primary_key=True)
    subtype = models.ForeignKey(
        'SubType',
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='category'
    )


class SubType(models.Model):
    subtype_name = models.CharField(max_length=10, null=False)

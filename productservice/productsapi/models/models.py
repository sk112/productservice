from django.db import models


class ProductItem(models.Model):
    item_cat = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING
    )

    item_id = models.CharField(primary_key=True, max_length=10)
    item_desc = models.CharField(max_length=20)
    segment = models.CharField(max_length=1)
    # photo = models.ImageField(max_length=100)
    information = models.CharField(max_length=500, null=True)
    percentage_alchol = models.FloatField(null=True)
    temparate = models.FloatField(null=True)


class quantity(models.Model):
    item = models.ForeignKey(
        'ProductItem',
        on_delete=models.DO_NOTHING,
        primary_key=False,
        unique=False,
        related_name='quantity'
    )
    case_size_in_ml = models.FloatField()
    case_sale_rate = models.FloatField()
    bottle_mrp_rate = models.FloatField()
    bottle_in_case = models.IntegerField()

from django.db import models

class Item(models.Model):
    # purchaser name
    purchaser_name = models.CharField(max_length=200)
    # item description
    item_description = models.CharField(max_length=400)
    # item price
    item_price = models.IntegerField(default=0)
    # purchase count
    purchase_count = models.IntegerField(default=1)
    # merchant address
    merchant_address = models.CharField(max_length=600)
    # merchant name
    merchant_name = models.CharField(max_length=400)
    # date time
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
import io
import pandas as pd

from ..models import Item

def handle_uploaded_file(f):
    content = f.read()
    #df = pd.read_csv(io.BytesIO(wells), encoding='utf8', sep=" ", index_col="id", dtype={"switch": np.int8})
    try:
        data = pd.read_csv(io.BytesIO(content), sep="\t", header=0)
        return content
    except Exception as e:
        raise e

def parse_raw_content_file(f):
    # do somethinf with f
    parsed_content = f.read()
    return parsed_content

def save_to_db(data):
    item = Item.objects.create(**data)
    item.save()
"""
fruit = Fruit.objects.create(name='Apple')
>>> fruit.name = 'Pear'
>>> fruit.save()
>>> Fruit.objects.values_list('name', flat=True)

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
    pub_date = models.DateTimeField('date published')

"""


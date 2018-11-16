import io
import pandas as pd

from ..models import Item

def handle_uploaded_file(f):
    try:
        content = f.read()
        ok = check_file(content)
        if ok:
            data = raw_file_to_pandas(content)
            for _, row in data.iterrows():
                item_dict = row_to_db_item(row)
                saved = save_to_db(item_dict)
            return {
                'status': ok
            }
        else:
            return {
                'status': ok
            }

    except Exception as e:
        return {
            'status': False,
            'error': e
        }

# Checks if content is well parsed.
def check_file(content):
    return True

# Converts raw bytes string to pandas dataframe.
def raw_file_to_pandas(content):
    data = pd.read_csv(io.BytesIO(content), sep="\t", header=0, encoding='utf-8')
    new_columns = [ col.replace(' ', '_') for col in data.columns ]
    data.columns = new_columns
    return data

def row_to_db_item(row):
    item_dict = row.to_dict()
    return item_dict

# Saves each line of pandas dataframe to db.
def save_to_db(item_dict):
    try:
        new_item = Item.objects.create(**item_dict)
        new_item.save()
        return True
    except Exception:
        return False


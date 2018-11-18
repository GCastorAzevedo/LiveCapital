import io
import logging
import pandas as pd

logger = logging.getLogger(__name__)
# logger.error('Something went wrong!')

from ..models import Item

def handle_uploaded_file(f):
    try:
        content = f.read()
        ok = check_file(content)
        if ok:
            data = raw_file_to_pandas(content)
            content = []
            for _, row in data.iterrows():
                item_dict = row_to_db_item(row)
                saved = save_to_db(item_dict)
                if saved:
                    logger.info("saved new item to db: \n %s " % item_dict)
                    content.push(item_dict)
            return {
                'status': ok,
                'message': "Saved the following uploaded items.",
                'content': content
            }
        else:
            return {
                'status': ok,
                'message': "File format not recognized."
            }

    except Exception as e:
        return {
            'status': False,
            'message': "Could not open uploaded file.",
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


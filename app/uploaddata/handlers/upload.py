import io
import pandas as pd

def handle_uploaded_file(f):
    content = f.read()
    #df = pd.read_csv(io.BytesIO(wells), encoding='utf8', sep=" ", index_col="id", dtype={"switch": np.int8})
    try:
        data = pd.read_csv(io.BytesIO(content), sep="\t", header=0)
        return content
    except Exception as e:
        raise e
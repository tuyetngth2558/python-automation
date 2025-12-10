import pandas as pd
import numpy as np

data = {
    'product_id': [101, 102, 103, 101, 104, 102, 101],
    'category': ['Ao', 'Quan', 'Giay', 'Ao', 'Mu', 'Quan', 'Ao'],
    'rating': [5, 3, np.nan, 4, 2, np.nan, 5], # Có rating bị rỗng
    'comment': ['Tot', 'Tam duoc', 'Dep', 'Ok', 'Xau', 'Rach', 'Tot']
}

df = pd.DataFrame(data)
df.to_csv('reviews.csv', index=False)
print("File reviews.csv đã sẵn sàng!")
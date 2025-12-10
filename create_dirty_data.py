import pandas as pd
import numpy as np # Thư viện toán học để tạo giá trị rỗng (NaN)

data = {
    'order_id': [1, 2, 3, 4, 5, 5, 6], # Để ý số 5 bị lặp lại
    'customer': ['An', 'Binh', np.nan, 'Dung', 'An', 'An', 'Hoa'], # np.nan là giá trị Rỗng
    'amount': [100, 200, 150, np.nan, 100, 100, 300], # Có giá trị rỗng
    'status': ['Shipped', 'Pending', 'Shipped', 'Cancelled', 'Shipped', 'Shipped', 'Pending']
}

df = pd.DataFrame(data)
df.to_csv('dirty_orders.csv', index=False)
print("--- ĐÃ TẠO FILE DỮ LIỆU BẨN THÀNH CÔNG ---")
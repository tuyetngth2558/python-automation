import pandas as pd
import random

# Tạo dữ liệu giả lập cho 20 đơn hàng
data = {
    'order_id': range(1, 21),
    'status': random.choices(['Shipped', 'Cancelled', 'Processing'], k=20),
    'amount': [random.randint(10, 100) for _ in range(20)], # Giá tiền từ 10$ đến 100$
    'country': random.choices(['Vietnam', 'USA', 'China'], k=20)
}

# Chuyển thành bảng (DataFrame)
df = pd.DataFrame(data)

# Lưu ra file CSV (Excel)
df.to_csv('orders.csv', index=False)

print("--- ĐÃ TẠO FILE orders.csv THÀNH CÔNG! ---")
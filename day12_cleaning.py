import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv('dirty_orders.csv')
print("=== DỮ LIỆU GỐC (BẨN) ===")
print(df)

# 2. Kiểm tra dữ liệu bị thiếu (Missing Values)
print("\n--- Kiểm tra số lượng ô bị trống ---")
print(df.isnull().sum()) 

# 3. Xử lý thiếu: Điền vào chỗ trống
# Nếu tên khách bị trống -> Điền "Unknown"
df['customer'] = df['customer'].fillna('Unknown')
# Nếu tiền bị trống -> Điền 0
df['amount'] = df['amount'].fillna(0)

# 4. Xử lý trùng lặp (Duplicates)
# Xóa các dòng bị trùng hoàn toàn
df_clean = df.drop_duplicates()

print("\n=== DỮ LIỆU SAU KHI LÀM SẠCH ===")
print(df_clean)

# 5. Lưu lại file sạch
df_clean.to_csv('clean_orders.csv', index=False)
print("\n-> Đã lưu file sạch ra 'clean_orders.csv'")
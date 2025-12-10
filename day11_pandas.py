import pandas as pd

# 1. LOAD: Đọc dữ liệu từ file (Giống FROM table)
df = pd.read_csv('orders.csv')

print("\n=== 1. XEM 5 DÒNG ĐẦU (Giống SELECT * LIMIT 5) ===")
print(df.head(5))

print("\n=== 2. CHỌN CỘT (Giống SELECT status, amount) ===")
# SQL: SELECT status, amount FROM table
print(df[['status', 'amount']].head(3))

print("\n=== 3. LỌC DỮ LIỆU (Giống WHERE) ===")
# SQL: WHERE status = 'Shipped' AND amount > 50
filter_condition = (df['status'] == 'Shipped') & (df['amount'] > 50)
shipped_high_value = df[filter_condition]
print(shipped_high_value)

print("\n=== 4. SẮP XẾP (Giống ORDER BY amount DESC) ===")
# SQL: ORDER BY amount DESC
sorted_df = df.sort_values(by='amount', ascending=False)
print(sorted_df.head(3))

print("\n=== 5. TÍNH TOÁN (Giống AGGREGATE) ===")
# SQL: SELECT SUM(amount), AVG(amount)
total_money = df['amount'].sum()
avg_money = df['amount'].mean()
print(f"Tổng tiền: {total_money} $")
print(f"Trung bình: {avg_money} $")
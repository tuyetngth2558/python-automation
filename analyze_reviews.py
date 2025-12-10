import pandas as pd

df = pd.read_csv('reviews.csv')
print("=== DỮ LIỆU GỐC ===")
print(df)

df['rating'] = df['rating'].fillna(0)

print("\n=== ĐIỂM TRUNG BÌNH THEO LOẠI ===")

avg_by_category = df.groupby('category')['rating'].mean()
print(avg_by_category)

sorted_df = avg_by_category.sort_values(ascending=False)
print("\n=== LOẠI SẢN PHẨM TỐT NHẤT ===")
print(sorted_df.head(1))
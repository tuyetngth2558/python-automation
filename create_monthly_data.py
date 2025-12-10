import pandas as pd

# Tạo 3 file riêng biệt
df1 = pd.DataFrame({'month': ['Jan', 'Jan'], 'revenue': [100, 120]})
df2 = pd.DataFrame({'month': ['Feb', 'Feb'], 'revenue': [110, 130]})
df3 = pd.DataFrame({'month': ['Mar', 'Mar'], 'revenue': [140, 150]})

df1.to_csv('sales_jan.csv', index=False)
df2.to_csv('sales_feb.csv', index=False)
df3.to_csv('sales_mar.csv', index=False)
print("Đã tạo 3 file tháng!")
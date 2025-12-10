import pandas as pd

print("🤖 ĐANG GỘP BÁO CÁO QUÝ 1...")

try:
    df1 = pd.read_csv('sales_jan.csv')
    df2 = pd.read_csv('sales_feb.csv')
    df3 = pd.read_csv('sales_mar.csv')

    df_total = pd.concat([df1, df2, df3])

    total_revenue = df_total['revenue'].sum()

    df_total.to_csv('Q1_Full_Report.csv', index=False)

    print(f"""
    ✅ XỬ LÝ THÀNH CÔNG!
    - Tổng doanh thu Quý 1: {total_revenue} $
    - Đã xuất file tổng hợp ra: Q1_Full_Report.csv
    """)

except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy file csv! Bạn đã chạy file 'create_monthly_data.py' chưa?")
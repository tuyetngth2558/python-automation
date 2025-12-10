import pandas as pd

# --- PHẦN 1: CHẾ TẠO ROBOT (Định nghĩa hàm) ---
def process_sales_data(input_file, output_file):
    print(f"\n🤖 ĐANG KHỞI ĐỘNG ROBOT XỬ LÝ FILE: {input_file}...")
    
    # 1. Đọc dữ liệu
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        return "❌ Lỗi: Không tìm thấy file đầu vào!"

    # 2. Làm sạch (Quy trình chuẩn hóa)
    initial_rows = len(df)
    df = df.drop_duplicates() # Xóa trùng
    df['amount'] = df['amount'].fillna(0) # Điền tiền thiếu
    clean_rows = len(df)
    
    # 3. Tính toán báo cáo
    total_revenue = df['amount'].sum()
    valid_orders = df[df['amount'] > 0].shape[0]

    # 4. Xuất file sạch
    df.to_csv(output_file, index=False)
    
    # 5. Trả về kết quả báo cáo
    report = f"""
    ✅ XỬ LÝ THÀNH CÔNG!
    - Dòng gốc: {initial_rows} -> Dòng sạch: {clean_rows}
    - Đã loại bỏ: {initial_rows - clean_rows} dòng trùng/rác.
    - Tổng doanh thu: {total_revenue} $
    - Số đơn hợp lệ: {valid_orders}
    - File sạch đã lưu tại: {output_file}
    """
    return report

# --- PHẦN 2: CHẠY THỬ NGHIỆM ---
# Giả sử hôm nay sếp gửi file 'dirty_orders.csv' (File hôm qua tạo)
ket_qua = process_sales_data('dirty_orders.csv', 'report_day13.csv')

# In báo cáo ra màn hình
print(ket_qua)
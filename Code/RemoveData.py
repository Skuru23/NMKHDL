import pandas as pd

# Đọc dữ liệu từ tệp hotelFinish.csv
hotel = pd.read_csv("../Data/hotelFinish.csv")

# Lọc bỏ các hàng không có thông tin số phòng hoặc số sao
hotel = hotel.dropna(subset=['Số lượng phòng', 'Rate Star'])

# Chuẩn hóa cột 'Rate Star'
hotel['Rate Star'] = hotel['Rate Star'].apply(lambda x: int(x) if x % 1 == 0.5 else x)

# Thay dấu phẩy bằng dấu chấm trong các cột điểm số
columns_to_clean = ["Độ sạch sẽ", "Dịch vụ", "Tiện nghi", "Vị trí", "Sự thoải mái và chất lượng phòng"]
for col in columns_to_clean:
    hotel[col] = hotel[col].astype(str).str.replace(",", ".").astype(float)

# Lưu dữ liệu đã xử lý vào tệp hotelFinish1.csv
hotel.to_csv("../Data/hotelFinish1.csv", index=False)

print(f"Lưu dữ liệu đã xử lý vào tệp hotelFinish1.csv")

import pandas as pd

# Đọc dữ liệu từ tệp hotel.csv
hotel = pd.read_csv("../Data/hotel.csv")
links = hotel['link'].tolist()

# Các từ khóa không liên quan đến khách sạn
keywords = [
    "motel", "hostel", "-room-", "nha-nghi", "nha-khach", "chung-cu",
    "-home-", "studio", "can-ho", "apartment", "house", "homestay",
    "villa", "resort"
]

# Lọc các liên kết không chứa các từ khóa không liên quan
filtered_links = [link for link in links if not any(keyword in link for keyword in keywords)]

# Lưu các liên kết còn lại vào tệp hotelNew.csv
filtered_links_df = pd.DataFrame(filtered_links, columns=['link'])
filtered_links_df.to_csv('../Data/hotelNew.csv', index=False)

print(f"Lưu {len(filtered_links)} liên kết vào tệp hotelNew.csv")

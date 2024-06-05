import pandas as pd

def remove_data(oldDataFile: str, newDataFile: str):
    hotel = pd.read_csv(oldDataFile)
    hotel = hotel.dropna(subset=['Số lượng phòng', 'Rate Star'])

    columns_to_clean = ["Độ sạch sẽ", "Dịch vụ", "Tiện nghi", "Vị trí", "Sự thoải mái và chất lượng phòng"]
    for col in columns_to_clean:
        hotel[col] = hotel[col].astype(str).str.replace(",", ".").astype(float)

    hotel.to_csv(newDataFile, index=False)

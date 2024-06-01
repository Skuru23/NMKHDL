import csv

input_file = "hotelFinish.csv"
output_file = "output.csv"

date = "2024-05-30"
date1 = "2024-05-28"
date2 = "2024-05-27"

def replace_check_in(url, new_date):
    return url.replace("checkIn=2020-11-15", f"checkIn={new_date}")

with open(input_file, mode='r', newline='', encoding="utf8") as infile, open(output_file, mode='w', newline='', encoding="utf8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    i = 0

    for row in reader:
        original_url = row[0]
        if i == 500: 
            updated_url = replace_check_in(original_url, date2)
        elif i == 1000:
            updated_url = replace_check_in(original_url, date1)
        else :
            updated_url = replace_check_in(original_url, date)
        row[0] = updated_url
        writer.writerow(row)
        i = i + 1

print("Updated and saved to output.csv")

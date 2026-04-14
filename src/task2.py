import csv
import os

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[0] == "pink morsel":
                price = float(row[1].replace("$", ""))
                quantity = int(row[2])
                sales = price * quantity
                data.append([sales, row[3], row[4]])
    return data

folder_path = r"C:\dev\quantium-starter-repo\data"
all_sales_data = []
files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

for file in files:
    full_path = os.path.join(folder_path, file)
    all_sales_data.extend(read_csv(full_path))

output_path = r"C:\dev\quantium-starter-repo\data\task2.csv"

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile) 
    writer.writerow(["sales", "date", "region"])
    writer.writerows(all_sales_data)

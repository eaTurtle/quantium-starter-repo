import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [x for x in reader if x[0] == "pink morsel"]
        for row in data:
            row[1] = row[1].replace("$", "")
            row[1] = float(row[1]) * float(row[2])
            row.pop(2)
    return data

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

pink_morsels_data_0 = read_csv("C:\\dev\\quantium-starter-repo\\data\\daily_sales_data_0.csv")
write_csv("C:\\dev\\quantium-starter-repo\\data\\pink_morsels_data.csv", pink_morsels_data_0)

pink_morsels_data_1 = read_csv("C:\\dev\\quantium-starter-repo\\data\\daily_sales_data_1.csv")
write_csv("C:\\dev\\quantium-starter-repo\\data\\pink_morsels_data.csv", pink_morsels_data_1)

pink_morsels_data_2 = read_csv("C:\\dev\\quantium-starter-repo\\data\\daily_sales_data_2.csv")
write_csv("C:\\dev\\quantium-starter-repo\\data\\pink_morsels_data.csv", pink_morsels_data_2)
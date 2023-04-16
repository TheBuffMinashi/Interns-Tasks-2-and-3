import os
import csv

index_folder = os.path.join(os.getcwd(), "index")
csv_file_path = f"{os.getcwd()}/output.csv"

with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["filename", "laptop_title", "link_to_product", "price", "description"])

    for file_name in os.listdir(index_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(index_folder, file_name)
            with open(file_path, "r") as txt_file:
                content = txt_file.readlines()
                writer.writerow([file_name, content[0], content[1], content[2], content[3:-1]])

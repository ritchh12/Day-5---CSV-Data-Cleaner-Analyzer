import csv
import os 
from collections import Counter

file_path = r"D:\Downloads\New folder\Genre_Details - Genre_Details.csv"

with open(file=file_path,mode='r') as file :
    
    data = csv.DictReader(file)
    field_names = data.fieldnames
        
    rows = list(data)
   
    # finding duplicates and creating clean data

    seen = set()
    clean_rows =[]
    duplicates = []

    for row in rows:
        row_tuple = tuple(row.items())

        if row_tuple in seen:
            duplicates.append(row)
        else:
            clean_rows.append(row)
            seen.add(row_tuple)

    

    # finding missing values
    missing ={}

    for row in rows:
        for column,value in row.items():
            if value == "":
                missing[column] = missing.get(column,0) + 1
                row[column] = "N/A"
    
    

    column_names = data.fieldnames
    total_rows = len(rows)
    total_columns =len(data.fieldnames)
    file_name = os.path.basename(file_path)


    # *************************summary report*************************
    print(20*"*","CSV Report", 20*"*" ,"\n")
    print(f"{"File Name":<20}: {file_name:>20}")
    print(f'{"Total rows":<20}: {total_rows:>20}')
    print(f'{"Total columns":<20}:{total_columns:>20}')
    print(f"{"Columns":<20}: {column_names}")
    print(f"{"Duplicate values":<20}: {duplicates}\n")

    if missing.items():
        print('Null values per column:-')
        for k,v in missing.items():
            print(f"{k} :{v}")
    print(50*"*")

#cleaned csv

with open("cleaned.csv",mode="w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader() #writing the headers
    writer.writerows(clean_rows) #writing the rows

    


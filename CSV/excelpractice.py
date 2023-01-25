import csv

with open('C:\Github_Local\Python\CSV\SampleCSVFile.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    col_index = header.index('Eldon Base for stackable storage shelf, platinum')

    for row in reader:
        value = row[col_index]
        print (value)
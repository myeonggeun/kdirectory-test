# import csv
import csv
from kdata import *
# read csv file to a list of dictionaries
with open('data.csv', 'r', encoding='utf-8-sig' ) as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
    
Korea_directory = data
print(Korea_directory)
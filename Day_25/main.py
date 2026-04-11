import csv
import re
with open('weather_data.csv', 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    contenu = f.read()
    temperatures  = re.findall(r'\d+', contenu)
    for lines in data:
        print(lines)
    for number in temperatures:
        print(number)
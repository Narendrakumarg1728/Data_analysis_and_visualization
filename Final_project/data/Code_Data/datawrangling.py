import xlrd
import time
import re
from collections import defaultdict


def get_country_name(country):
    codebook = xlrd.open_workbook('country_codes.xlsx')
    sheet = codebook.sheet_by_name('country_codes')
    
    for i in xrange(1,sheet.nrows):
        row = sheet.row_values(i)
        if country == str(row[0])[:-2]:
            return str(row[1])
    

print time.strftime("%H:%M:%S") 
book = xlrd.open_workbook('Morticd10_part1.xlsx')
print time.strftime("%H:%M:%S")



sheet = book.sheet_by_name('Morticd10_part1')

data = defaultdict(lambda: defaultdict(dict))


for i in xrange(1,sheet.nrows):
    row = sheet.row_values(i)
    cause = str(row[5])
    regex = r"(^(C\d\d))|(^(D[0-4][0-9]))"
    # Capture data only if the cause is Cancer. The codes for cancer ranges from C00-D49
    if re.compile(regex).match(cause):
        country = str(row[0])[:-2]
        country_name = get_country_name(country)
        year = str(row[3])[:-2]
        sex = row[6]
        deaths = row[9]
        if year in data:
            if country_name in data[year]:
               data[year][country_name]['death'] += deaths
               if sex == 1:
                   data[year][country_name]['Male'] += deaths
               elif sex == 2:
                   data[year][country_name]['Female'] += deaths               
            else:
                data[year][country_name]['death'] = deaths
                if sex == 1:
                    data[year][country_name]['Male'] = deaths
                    data[year][country_name]['Female'] = 0
                elif sex == 2:
                    data[year][country_name]['Female'] = deaths
                    data[year][country_name]['Male'] = 0                    
        else:
            print country_name,year,i
            data[year][country_name] ={'death':deaths}
            if sex == 1:
                data[year][country_name]['Male'] = deaths
                data[year][country_name]['Female'] = 0
            elif sex == 2:
                data[year][country_name]['Female'] = deaths
                data[year][country_name]['Male'] = 0
                          
            
	
print data
print time.strftime("%H:%M:%S")
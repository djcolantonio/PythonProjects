import openpyxl, os, pprint

os.chdir("C:\\Users\\Dan\\AppData\\Local\\Programs\\Python\\Python36-32\\MyDataFiles")
print('Opening workbook...')

workbook = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = workbook.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading data...')
for row in range(2, sheet.max_row + 1):
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	population = sheet['D' + str(row)].value
		      
	countyData.setdefault(state, {})
	countydata[state].setdefault(county,{'tracts': 0, 'population': 0})
		      
	countyData[state][county]['tracts'] +=1
	countyData[state][county]['population'] += int(population)
		      
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')


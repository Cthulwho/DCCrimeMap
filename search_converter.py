import re
import csv

#these are the regexes that match the time formats
patterns = ['[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]', '[0-9]\:[0-9][0-9]\:[0-9][0-9]']

with open('sr4.csv', 'r') as infile:
	outfile = open('Crime_Out.csv', 'w')
	reader = csv.DictReader(infile, delimiter = ',')
	writer = csv.writer(outfile, delimiter = ',')
	for row in reader:
		match = re.search('(([0-9][0-9])|[0-9])\:', row['REPORT_DAT'])
		if not match:
			print('No Match Found')
		else:
			writer.writerow([('2010-1-1 ' + match.group(0) + '00:00'), ('2010-1-1 ' + match.group(0) + '00:10'), row['XBLOCK'], row['YBLOCK']])
	outfile.close()
	infile.close()
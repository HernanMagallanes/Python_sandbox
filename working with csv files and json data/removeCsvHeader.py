import csv
import os

# step 1: Loop through each CSV file
os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    # step 2: Read in the CVS file

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # step 3: Write out the CSV file without the first row
    csvFileObj = open(os.path.join('headerRemoved', csvFilename),
                      'w',
                      newline='')
    csvWriter = csv.writer(csvFileObj)

    for row in csvRows:
        csvWriter.writerow(row)

    csvFileObj.close()

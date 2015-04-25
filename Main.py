import csv

with open('GroceryDictionary.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('GroceryDictionary.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
        
for key in mydict:
    print key, 'corresponds to', mydict[key]

import csv

print 'read dictionary'
with open('GroceryDictionary.csv', mode='r') as infile:
    print 'read 1'
    reader = csv.reader(infile)
    mydict = dict(reader)

##    with open('GroceryDictionary.csv', mode='w') as outfile:
#        print 'read 2'
#        writer = csv.writer(outfile)
#        mydict = {rows[0]:rows[1] for rows in reader}
        
print 'iterate'
for key in mydict:
    print key

import csv
import sys

print 'read dictionary'
with open('GroceryDictionary.txt', mode='r') as infile:
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
    
while 1:
    val = sys.stdin.read(1).rstrip('\n')
    if (val == 'q'):
        sys.exit()
    print(mydict[val])

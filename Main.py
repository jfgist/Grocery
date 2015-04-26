import csv
import sys

print 'read dictionary'
with open('GroceryDictionary.txt', mode='r') as infile:
    print 'read 1'
    reader = csv.reader(infile)
    mydict = dict(reader)
        
print 'iterate'
for key in mydict:
    print key
    

print 'Type "quit" to exit.'
while (True):
  line = raw_input('PROMPT> ')
  if line == 'quit':
    sys.exit()
  print(line)
  print(mydict[line])

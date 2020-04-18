import csv

# dummy dictionary with values
dict = {'dictvalue1' : ['status : online ', 'availability : up'], 'dictvalue2' : ['status : offline', 'availability : shutdown']}

# create a list containing the keys of each dictionary
keys = list(dict.keys())

#opens a new file
with open('dict-to-csv.csv', mode='w', newline='') as csv_file:

    #creates a list with the following values
    fieldnames = ['ID', 'status', 'availability']

    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Create an object which operates like a regular writer but maps dictionaries onto output rows.
    #The fieldnames parameter is a sequence of keys that identify the order in which values in the
    #dictionary passed to the writerow() method are written to file f
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)


    writer.writeheader()
    for k in range(len(keys)):
     print(keys[k])
     for i in (dict[keys[k]]):
      if ("status" in i):
         status = i
         print( "this is in the first list", status)
      elif ("availability" in i):
          availability = i
          print("this is in the second list", availability)
     print("writing row")
     writer.writerow(
        {'ID': keys[k], 'status': status, 'availability': availability})
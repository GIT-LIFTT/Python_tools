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

    #writes the headers
    #Write a row with the field names (as specified in the constructor).
    writer.writeheader()

    #as we defined earlier a list  of the keys from the opriginal dictionary
    # this allows us to iterate through each key : value pair
    # for k in the range of keys see above = 2
    for k in range(len(keys)):
     print(keys[k])

     #  a for loop within a for loop  allows us to iterate through the elements within the current key
     for i in (dict[keys[k]]):

      # if string value which = status is found assing to the varible i
      if ("status" in i):
         status = i
         print( "this is in the first list", status)
      elif ("availability" in i):
          availability = i
          print("this is in the second list", availability)
     print("writing row")

     #write a row with the current values of the varibles within the given for loop
     writer.writerow(
        {'ID': keys[k], 'status': status, 'availability': availability})
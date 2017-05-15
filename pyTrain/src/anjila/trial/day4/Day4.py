'''
Created on May 14, 2017

@author: rujina
'''
#--------------- read write file -------------------
import csv, json
import urllib2


# with open('FL_insurance_sample.csv','rb') as csv_data:
#     read_data=csv.reader(csv_data)
#     print read_data
#     for data in read_data:
#         print data[0], data[1]
with open('test.json', 'rb') as csv_data:
    read_data = json.load(csv_data)
    print read_data
    with open('write.json', 'wb') as json_date:
        mydata = json.dump(read_data, json_date)
#     for data in read_data:
#         print data[0], data[1]

#------------------------api_read----------------------------
url = "http://api.icndb.com/jokes/random"
data = urllib2.urlopen(url)
for i in data:
    print i

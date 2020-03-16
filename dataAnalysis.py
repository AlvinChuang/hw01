# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = 'sample_input.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
####target_data = data[:10]

data = sorted(data, key=lambda i: i['station_id']) #sort data by station_id
#print(data) #checking
output_data = [] #the output
while len(data) != 0 : #until the data is empty, which means that all the stations have been handled
   target_station = data[0]['station_id'] #get first station in data as target
   target_data = list(filter(lambda item: item['station_id'] == target_station, data)) #get all the record of the target station
   #print(target_data) #checking

   target_data = list(filter(lambda del_99: del_99['WDSD'] != '-99.000', target_data)) #delete the ones that WDSD=-99.000
   target_data = list(filter(lambda del_99: del_99['WDSD'] != '-999.000', target_data)) #delete the ones that WDSD=-999.000

   target_data = sorted(target_data, key=lambda i: i['WDSD']) #sort target_data by WDSD
   #print(target_data) #checking
   if len(target_data)>=2 :
      output_data.append([target_station, float(target_data[-1]['WDSD']) - float(target_data[0]['WDSD'])])
   else :
      output_data.append([target_station, 'None'])

   data = list(filter(lambda del_item: del_item['station_id'] != target_station, data)) #delete the target station from the data
   #remaining data are stations that haven't been hadled yet
print(output_data)

#=======================================

# Part. 4
#=======================================
# Print result
#if len(target_data) == 0 :
#   print('None')
#else :
#   print(target_data)
#========================================
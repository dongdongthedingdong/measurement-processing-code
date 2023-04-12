import csv

temperature = []
num_of_lines_to_process = 10000
biggestNumber = 0
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          temperature.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
print(f' The biggest temperature is {biggestNumber} *Celsius.')
print(f'temperature is {temperature[3251][0]} at {temperature[3251][1]}' )


temperature = []
num_of_lines_to_process = 10000
smallestNumber = 0
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          temperature.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    
print(f' The smallest temperature is {smallestNumber} *Celsius.')

print(f'temperature is {temperature[2239][0]} at {temperature[2239][1]}' )

pressures = []
num_of_lines_to_process = 10000
smallestNumber = 0
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    
print(f' The smallest pressure is {smallestNumber} *hPa.')

print(f'pressure is {pressures[3045][0]} at {pressures[3045][1]}' )


pressures = []
num_of_lines_to_process = 10000
smallestNumber = 0
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
          
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
  
print(f' The biggest pressure is {biggestNumber} *hPa.')

print(f'pressure is {pressures[14733][0]} at {pressures[14733][1]}' )

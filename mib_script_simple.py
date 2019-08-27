# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:17:39 2019

@author: User
"""


#==============================================================================
# Steps to activate the automotatic SST and parameters script:
# 1. Copy the information from one Sub System (All coloums) to excel
# 2. Save the excel file by name: "TLC.csv" as a *comma delimited csv* file
# 3. Run the program by double clicking it
# 4. Mark the result from the cmd, and copy it by right clicking the upper bar
#    and choosing the "Copy option"
#==============================================================================
import csv
def read_csv(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data =[]
        for row in csv_reader:
            data.append(row)
    return data
    
def sst_data(sst_value,sst_name):
    sst_text = "<ServiceSubtype Value=\""+sst_value+"\" Name=\""+sst_name+"\">\n"
    return sst_text

def parameter_data(param_name,param_type,param_unit,param_little ="false"):
    param_text = "  <Parameter Name=\""+param_name+"\" Type=\""+param_type+"\" Unit=\""+param_unit+"\" IsLittleEndian=\"" +param_little+ "\" />\n"
    return param_text

source_file = "TLC.csv" ###Write here the name of the new file
data = read_csv(source_file)

result=""
for row in range(0, len(data)):
    if(data[row][1]!=''):
        if (row>0):
            result += "</ServiceSubtype>\n\n"
        result += sst_data(data[row][3],data[row][1])
    else:
        param_name = data[row][5]
        param_type = data[row][6]
        param_unit = data[row][7]
        result+=parameter_data(param_name,param_type,param_unit)
result += "</ServiceSubtype>\n\n"
print(result)
input("Press Enter to continue...")
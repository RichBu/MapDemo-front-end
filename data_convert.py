"""
This program converts data clip to a MySQL data seed file.

Opens CSV cleans up the data and then outputs to a 

By Rich Budek 03/05/2020 in Python 3.8
"""


import pandas as pd
import numpy as np
import jinja2
import math
import re


class Config_Data:
    #set up by user once
    filepath = "Z:\Shared Folders\Data\Recreis\Data Files"
    filename_act = "data_act.csv"
    fileout_01 = "act_seed.sql"
    filename_loc = "data_loc.csv"
    fileout_02 = "loc_seed.sql"


class Project_Data:
    #data that gets transferred between functions
    full_filename_act = ""
    file_act_is_csv = False
    full_filename_out_01 = ""

    full_filename_loc = ""
    file_loc_is_csv = False
    full_filename_out_02 = ""



class Act_In:
    id = 0
    name = ""
    live = True
    created_at = ""
    updated_at = ""
    absolute_min_players = 0
    absolute_max_players = 0
    duration = 0
    default_min_players = 0
    default_max_players = 0
    icon_name = ""


class Loc_In:
    id = 0
    name = ""
    area = ""
    address = ""
    venue_type = ""
    is_outdoor = True
    phone = ""
    cost = ""
    activity_id = 0
    activity_accomodations = ""
    quality = 0
    created_at = ""
    updated_at = ""
    longitude = -1.0
    latitude  = 1.0
    image1 = ""
    image2 = ""
    image3 = ""
    activity_name = ""
    distance_from_center = 0.0


def convertDFtoSeedStr( dbName, tblName, dfFileIn ):
    #convert to seed strings
    #returns seed strings
    pass

    #function to create all the seed strings
    db_fieldnamestr1 = 'id'
    row = dfFileIn.head(1)
    for (columnName, columnData) in row.iteritems():
        db_fieldnamestr1 = db_fieldnamestr1 + ', ' + columnName.strip()
    print ('field name str =')
    print (db_fieldnamestr1, '\n')
    
    #create the seed string 
    db_file = dbName    #get from mySQL lab
    db_table1 = tblName
    #db_fieldnamestr1 = 'id, name, live, created_at, updated_at, absolute_min_players, absolute_max_players, duration, default_min_players, default_max_players, icon_name'
    seedstr = []
    seedstr.append('')
    seedstr.append('USE '+ db_file + ';')
    seedstr.append('')


    for index, row in dfFileIn.iterrows():
        print ("row = {:d}".format(index) )
        temp_start_chr = ''   #for first entry no comma
        tempstr = ""
        seedstr.append('')
        seedstr.append('INSERT INTO ' + db_table1 + ' (')
        seedstr.append(db_fieldnamestr1)
        seedstr.append(') VALUES (')
        temp_start_chr =  "{:d}".format( index ) + ' , '    #id field is index variable

        for (columnName, columnData) in row.iteritems():
            print(columnName, ':', columnData, '/')
            tempstr = tempstr + temp_start_chr
            print (type(columnData) )
            temp_data_str = ''
            if (type(columnData) is bool):
                temp_data_str = ' true '
            if (type(columnData) is float):
                temp_data_str = " {:f} ".format( columnData )
            if (type(columnData) is int):
                temp_data_str = " {:d} ".format( columnData )
            if (columnData != columnData):
                temp_data_str = ' "' + '" '
            if (type(columnData) is str):
                temp_data_str = ' "' + columnData.strip() + '" '
            tempstr = tempstr + temp_data_str    #do we need to strip
            temp_start_chr = ','
        #finshed with a row
        print (tempstr)
        seedstr.append(tempstr)
        seedstr.append(');')
        print ("\n")


    seedstr.append('')
    seedstr.append('')
    seedstr.append('')


    return seedstr




#main function or run
def main():
    #this is the "main" program

    #print welcome
    print(" ")
    print("Convert CSV to seed file")
    print("by Rich Budek")
    print(" ")

    #setup needed variables
    config_data = Config_Data()
    project_data = Project_Data()

    #create all the full file path names here, so only have to do it once
    project_data.full_filename_act = config_data.filepath + "\\" + config_data.filename_act
    if project_data.full_filename_act[-3:].lower() == 'csv':
        project_data.file_act_is_csv = True
    else:
        project_data.file_act_is_csv = False
    project_data.full_filename_out_01 = config_data.filepath + "\\" + config_data.fileout_01

    project_data.full_filename_loc = config_data.filepath + "\\" + config_data.filename_loc
    if project_data.full_filename_loc[-3:].lower() == 'csv':
        project_data.file_loc_is_csv = True
    else:
        project_data.file_loc_is_csv = False
    project_data.full_filename_out_02 = config_data.filepath + "\\" + config_data.fileout_02

    #these are all the data tables
    activities = []
    locations = []

    #read in the existing activies file
    if project_data.file_act_is_csv:
        #FUTURE read in csv file
        pass
        activities = pd.read_csv(project_data.full_filename_act,index_col=0, skiprows=0)
    else:
        activities = pd.read_excel(project_data.full_filename_act)
    activities_len = len(activities.index)
    print ("number of activities imported = {:d}".format( activities_len ) )

  

    db_file = 'vlbk7122d7cbev23'    #get from mySQL lab
    db_table1 = 'activities'
    db_table2 = 'locations'

   
    outputStrings = convertDFtoSeedStr( db_file, db_table1, activities )




    #write activities file to text file
    file1 = open(project_data.full_filename_out_01, "w+")
    
    for string in outputStrings:
        file1.write(string+'\n')
    file1.close()

    #print (activities)

    #read in the locations
    if project_data.file_loc_is_csv:
        #FUTURE read in csv file
        locations = pd.read_csv(project_data.full_filename_loc,index_col=0, skiprows=0)
    else:
        locations = pd.read_excel(project_data.full_filename_loc)

    locations_len = len(locations.index)
    print ("number of locations imported = {:d}".format( locations_len ) )


    outputStrings2 = convertDFtoSeedStr( db_file, db_table2, locations )

    #write locations file to text file
    file2 = open(project_data.full_filename_out_02, "w+")
    
    for string in outputStrings2:
        file2.write(string+'\n')
    file2.close()

    #print (locations[1])




print (" ")
print (".Program start.")

if __name__ == "__main__":
    main()
    print (".Program end.")






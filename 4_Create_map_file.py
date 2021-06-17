#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:22:55 2021

@author: katinka
"""

"""
Takes the MAP_INPUT_FILE (output from previous file), and creates the proper format

: 4 columns [1: CHR, 2: "0", 3: SNP-ID, 4:BP position]


"""
import math

def create_map(fh_MAP2, output_MAP):
    MAP_FILE = open(output_MAP, 'w')  #open output file
    fh_filtered_file = open(fh_MAP2, "r")  #open the file I made from the previous script
    for LN, line_map in enumerate(fh_filtered_file):  #Go through it line by line
        temp_line2=line_map.rstrip('\n').split('\t')  #split by tab
        if temp_line2[1].startswith("Chromosome0"):  #if the (chromosomeline) starts with chromosome0, include the last number 
            CHR1_9 = temp_line2[1]
            if LN == 0:
                MAP_FILE.write(CHR1_9.lstrip("Chromosome0") + "\t" )
            else:
                MAP_FILE.write(CHR1_9.lstrip("Chromosome0") + "\t")
        elif temp_line2[1].startswith("Chromosome"):  #go through the headers line by line and if they start with Chromosome, we remove and add the rest to the list
            CHR10_18 = temp_line2[1]
            if LN == 0:

                MAP_FILE.write(CHR10_18.lstrip("Chromosome") + "\t")
            else:
                MAP_FILE.write(CHR10_18.lstrip("Chromosome") + "\t")
            
        if LN == 0:
            MAP_FILE.write(temp_line2[0] + "\t" + "0" + "\t" +str(math.ceil(int(temp_line2[9])-int(temp_line2[3])/int(2)))) #add the information in following order: chromosome, ID, 0(for centimorgan position and, bp-pos)
        else:
            MAP_FILE.write(temp_line2[0] + "\t" +"0" +"\t" +str(math.ceil(int(temp_line2[9])-int(temp_line2[3])/int(2))))
        MAP_FILE.write("\n")
    
    MAP_FILE.close()
    
    fh_filtered_file.close()
   
    return 0
#fh_MAP2 = "MAP_v7_input.tsv"
#output_MAP = "MAP_v7.map"
#create_map(fh_MAP2, output_MAP)

import sys
print("fromjupyter")
if __name__ == "__main__":
    #SNP_chr, SNP_pos, N_of_bp, file
    
    print("from_commandline")

    
    for varg in range(len(sys.argv)):
        print('Argument ' + str(varg) + ': ' + str(sys.argv[varg]))
        print('Function')
    if len(sys.argv) < 2:
        print('Not enough arguments')
    else:
        print('Running: functions(' + str(sys.argv[1]) + ', 2)')      
        create_map(sys.argv[1], sys.argv[2])
        





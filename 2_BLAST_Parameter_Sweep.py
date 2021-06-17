#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:34:27 2021

@author: katinka
"""
"""
This function takes the BLAST (BLAST output format 6) result file and the file containing all SNP id's
Chromosome_id_file) as an input.
The blast-result file was created by blasting the 151 sequences created for each marker onto the reference genome of interest.

The purpose of the function is to test the parameters "percantage similarity" and "sequence allignment length"
derived from the BLAST results (sim_percentage, marker_length), and find the value of the two parameters
combined that best in order to retain the highest possible amount of "good markers" (Explained in the thesis under "methods")

"""



def filter_function(Blast_result_file, sim_percentage, marker_length, Chromosome_id_file):
    seen_once = []
    chr_id_list = []
    more_than_once = []
    
    fh_Chromosome_id_file = open(Chromosome_id_file, "r")
    for line_so in fh_Chromosome_id_file:  #going through the Marker ID's and create a list of 0's for every incident.
        seen_once.append(0)  
        more_than_once.append(0)  #this is done as well to later count the incidents that are "seen twice or more"
        chr_id_list.append(line_so.rstrip('\n'))
    fh_Chromosome_id_file.close()
    
    fh_Blast_result_file = open(Blast_result_file, "r")  #open blast result file
    for vl, line in enumerate(fh_Blast_result_file):
        if vl % 1000 == 0:  #line to keep count in the terminal output
            print("p1: " + str(marker_length) + ", p2: " + str(sim_percentage) + ", line: "+ str(vl))
        temp_line=line.strip().split('\t')
        if float(temp_line[3]) >= float(marker_length) and float(temp_line[2]) >= float(sim_percentage):  #filtering settings
            for vi, item in enumerate(chr_id_list):
                if item == temp_line[0]:  #compare SNP ID's
                    if seen_once[vi] == 0:  
                        seen_once[vi] = 1  # if seen once on that line number is equal to zero -> write a 1 on "seen once"
                    else: 
                        more_than_once[vi] = 1  # if seen once is already = 1, (it means that the SNP has passed the thresholds tested before), then add 1 to the list of "seen_more"
                    
    fh_Blast_result_file.close()
    return sum(seen_once), sum(more_than_once)

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



    ## insert parameters of base pair length and base pair similarity %, that you want to investigate:
        
    #bp_length = [60, 70, 80, 90, 110, 120, 130]
    #perc_sim = [99, 100 ]
    #bp_length = [149, 150, 151]
    perc_sim = [95, 96, 97, 98, 99, 100 ]
    bp_length = [80, 90, 110, 120, 130, 140, 150, 151]
    #perc_sim = []
    #vi1 = 80.5
    #while vi1 <= 86.5:
        #perc_sim.append(vi1)
        #vi1 += 0.5
    list_of_lists_seen_once = []
    list_of_lists_seen_more = []
        
    fh = open("parameter_matrix_ver1_AM5V7.tsv", "w")
    fh2 = open("parameter_matrix_more_ver1_AMFV7.tsv", "w")
    fh.write('seen_once\t99\t100\n')
    fh2.write('seen_more\t99\t100\n')
    for line_bp_length in bp_length:

        list_seen_once = []
        list_seen_more = []
        fh.write(str(line_bp_length))
        fh2.write(str(line_bp_length))
        for vi, line_perc_sim in enumerate(perc_sim):
            seen_once, more_than_once = filter_function(sys.argv[1], line_perc_sim, line_bp_length, sys.argv[2])
            list_seen_once.append(seen_once)
            list_seen_more.append(more_than_once)
            #if vi == 0: 
            #   fh.write(str(seen_once))
            #   fh2.write(str(more_than_once))
            #else:
            fh.write("\t" + str(seen_once))
            fh2.write("\t" + str(more_than_once))
                
        list_of_lists_seen_once.append(list_seen_once)    
        list_of_lists_seen_more.append(list_seen_more)
        fh.write("\n")
        fh2.write("\n")
    fh.close() 
    fh2.close()              
    print(list_of_lists_seen_once, list_of_lists_seen_more)
    
  # The output is a matrix of occourences of seen once and seen twice, fraction can be calculated as described in the thesis.  

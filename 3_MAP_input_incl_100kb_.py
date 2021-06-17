#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:36:04 2021

@author: katinka
"""

"""
Before this script was run, the Parameter sweep was performed and the two values for %similarity and minimal marker length
were calculated.

These two values are inputs of this function, that takes the BLAST output and marker-ID's, and create
a file consisting of the entire BLAST output information of markers that contain markers with BLAST results,
that passes the parameter thresholds.

This output file is now the input file for the file that create the finished MAP file.

(If two markers (or more) have values that passes the paramter thresholds tested, and they are placed within 100 kb
then BOTH of the markers will be included as well, therefore a second step is needed to exclude duplicate SNP ID's and keep one of them) 

"""


def filter_function(BLAST_RESULT, min_seq_identity, min_marker_length, Chromosome_id_file, output_file):  
    fh_MAP = open(output_file, 'w')  #open output
    sc = "Scaffold"  #ignore scaffold for AM560
    seen_once = []
    seen_more = []
    chr_id_list = []
    classify_these = [] 

    
    fh_Chromosome_id_file = open(Chromosome_id_file, "r")  #open my chromosome ID's
    for line_so in fh_Chromosome_id_file:    #go through line b liine
        seen_once.append(0)  #append a "0" for every line iteration
        seen_more.append(0)
        chr_id_list.append(line_so.rstrip('\n'))  #make list of chromosome ID's - unnecessary??
    fh_Chromosome_id_file.close()
    
    fh_Blast_result_file = open(BLAST_RESULT, "r")  #open Blast results
    for vi, line in enumerate(fh_Blast_result_file):  #enumerate over the results
        temp_line=line.strip().split('\t')  #split by tab
        if sc not in temp_line[1]:  #remove Scaffold results 
            if float(temp_line[2]) >= int(min_seq_identity) and float(temp_line[3]) >= int(min_marker_length):  #filter by 100 % identity and 90 bp marker length
                for vi_id, line_id in enumerate(chr_id_list):  #enumerate over list of ID's 
                    if line_id == temp_line[0]:  #if ID from chr_file is present in BLAST file:
                        if seen_once[vi_id] == 0:  #and the enumeration LN 
                            seen_once[vi_id] = 1  #if it is seen once at the place, count 1
                            #fh_MAP.write(line)  #write the entire line into the map file
                        else:
                            seen_more[vi_id] = 1  #if it is seen more than once, append 1
                            #exclude_these_IDs.append(line_id)  #append all ID's that is seen more than once into a file
                            #print(seen_more[vi_id], exclude_these_IDs)  #try to exclude BOTH of these from the excisting file??
                            #fh_MAP.write('\n')  #line space char
    fh_Blast_result_file.close()
    
    fh_Blast_result_file = open(BLAST_RESULT, "r")  #open Blast results
    for vi, line in enumerate(fh_Blast_result_file):  #enumerate over the results
        temp_line=line.strip().split('\t')  #split by tab
        if sc not in temp_line[1]:  #remove Scaffold results 
            if float(temp_line[2]) >= int(min_seq_identity) and float(temp_line[3]) >= int(min_marker_length):  #filter by 100 % identity and 90 bp marker length
                for vi_id, line_id in enumerate(chr_id_list):  #enumerate over list of ID's 
                    if line_id == temp_line[0]:  #if ID from chr_file is present in BLAST file:
                        if seen_once[vi_id] == 1 and not seen_more[vi_id] == 1 :  #and the enumeration LN 
                            fh_MAP.write(line)  #write the entire line into the map file
                        if seen_once[vi_id] == 1 and seen_more[vi_id] == 1: 
                            classify_these.append(line)
                        else:
                            classify_these.append(line) 

    
    for vl, item in enumerate(classify_these):
        temp_item = item.rstrip("\n").split("\t")
        for vi, item in enumerate(classify_these):
            temp_item2 = item.rstrip("\n").split("\t")
            if temp_item2[0] == temp_item[0]:
                if temp_item[1] == temp_item2[1]:
                    if abs((int(temp_item[9])-((int(temp_item[9])-int(temp_item[8]))/int(2)))-(int(temp_item2[9])-((int(temp_item2[9])-int(temp_item2[8]))/int(2)))) < int(100000):
                        fh_MAP.write(item)




    fh_Blast_result_file.close()
    fh_MAP.close()
    return  
#BLAST_RESULT = "DUMMY_BLAST_RESULT.txt"
#Chromosome_id_file = "ID.txt"
#output_file = ""
#fh_MAP = filter_function(BLAST_RESULT, 100, 90, Chromosome_id_file)


       
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
        filter_function(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5])

        

        

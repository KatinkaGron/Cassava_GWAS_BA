#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:50:48 2021

@author: katinka
"""
"""
This function takes the transposed VCF file as an input, the file of with the individual-clone ID included in the study of Rabbi et al.
The file is reffered to as the "phenofile", but the file was actually produced to show the BLUB correlations between traits of each individual.
We use this file because it contains the CASSAVABASE_NAME and the GBS-identifyer name which is later needed to create the file of phenotypes.

The function creates a PED file, without information of the parents, the sex or the phenotype. These variables are replaced with a "0"

It does contain the Genotype information of each individual for all of the SNP's analysed. 


"""
import sys

def f_ped_production(transposed_VCF_file, phenofile, output_file, map_file):
    marker_found_in_map_file = []
    id_map = []
    cluster = []
    pheno_id = []
    pheno_id_cas = []
    count = 0

    fh_phenofile_guide = open(phenofile, 'r')
    for vi_phen, line_phen in enumerate(fh_phenofile_guide):  # open phenofile guide file with cycles and names
        if vi_phen > 2:  # skip initial 3 lines
            temp_line_pheno = line_phen.strip().split('\t')  # split phenoguide by tab, Access the individual ID's, icl.
            cluster.append(temp_line_pheno[6])
            pheno_id.append(temp_line_pheno[2])
            pheno_id_cas.append(temp_line_pheno[3])
    fh_phenofile_guide.close()  # close the file again
    
    fh_map_file = open(map_file, "r")  # open the finished map_file
    for vi_map, item_map in enumerate(fh_map_file):  # go through it
        temp_line_map = item_map.strip().split('\t')  # split by tab
        id_map.append(temp_line_map[1])  # append ID's in a list
    fh_map_file.close()  # close the file again
    
    id_map_set = set(id_map)
    pheno_id_map = {}
    for vi_ID, pheno_id_line in enumerate(pheno_id):
        #value = (cluster[vi_ID] + '\t' + pheno_id_cas[vi_ID] + '\t' + 
        #         pheno_father_id[vi_ID] + '\t' + pheno_mother_id[vi_ID] + 
        #         '\t' + "0" + '\t' + "0")
        value = (cluster[vi_ID] + '\t' + pheno_id_cas[vi_ID])
        pheno_id_map[pheno_id_line] = value
    
    fh_vcf_t_file = open(transposed_VCF_file, "r")  # Open the transposed vcf (PED file)
    fh_ped = open(output_file, "w")  # open output file
    for vi_line_vcf, line_vcf in enumerate(fh_vcf_t_file):  # go through it line by line #split it in columns
        temp_line_char = line_vcf.strip().split('\t')  # split by tab
        first_half_of_name = temp_line_char[0][0:len(temp_line_char[0])//2]  # cut names from transposed file
        if temp_line_char[0] == "REF":  # Store all the ref and alt nt's into lists
            vref = temp_line_char[:]
        elif temp_line_char[0] == "ALT":  # adding the alternative allele
            valt = temp_line_char[:]
        elif temp_line_char[0] == "ID":  # store all ID's into list
            ID = temp_line_char[:]
            for vi_ped, items_ped in enumerate(ID):  # enumerate over the ID's in the PED file                
                foundID = False
                if items_ped in id_map_set:
                    # if they are present, add a TRUE to the list
                    foundID = True
                    count +=1
                marker_found_in_map_file.append(foundID)
                print(len(marker_found_in_map_file))
                print(count)
                #print(foundID)
           #print(List_of_True)
        elif vi_line_vcf > 8:  # skipping initial 9 lines
            if first_half_of_name not in pheno_id_map:
                continue
            write_string = pheno_id_map[first_half_of_name]
            fh_ped.write(write_string)
            for column_vcf_t_file in range(1, len(temp_line_char)):  # iterate starting from 1 to length of the
                # line
                if marker_found_in_map_file[column_vcf_t_file]:  # If the marker was found in the map file then we
                    # can continue:
                    if temp_line_char[column_vcf_t_file] == "0/0":  # write references or alt after which symbol.
                        fh_ped.write('\t' + vref[column_vcf_t_file] + '\t' + vref[column_vcf_t_file])

                    elif temp_line_char[column_vcf_t_file] == "1/0":
                        fh_ped.write('\t' + valt[column_vcf_t_file] + '\t'+ vref[column_vcf_t_file])

                    elif temp_line_char[column_vcf_t_file] == "0/1":
                        fh_ped.write('\t' + vref[column_vcf_t_file] + '\t' + valt[column_vcf_t_file])

                    elif temp_line_char[column_vcf_t_file] == "1/1":
                        fh_ped.write('\t' + valt[column_vcf_t_file] + '\t' + valt[column_vcf_t_file])

                    else:
                        fh_ped.write('\tsomething went wrong\tsomething went wrong')
                        
                        raise ValueError('noget er galt')
            fh_ped.write('\n')  # new line character


                        
    print(count)                        
    # fh_MAP_FILE.close()
    fh_ped.close()

    fh_vcf_t_file.close()
    # fh_phenofile_guide.close()
    return 0
"""
map_file_main = "MAP_v6.map"
pheno_file_main = "pheno_dummy.txt"
transposed_VCF_file_main = "dummy_ped.tsv"
output_file_main = "new_ped.ped"
f_ped_production(transposed_VCF_file_main, pheno_file_main, output_file_main, map_file_main)
"""


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
        f_ped_production(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4])

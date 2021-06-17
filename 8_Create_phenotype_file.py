#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:44:15 2021

@author: katinka
"""

"""
This function, first takes the phenotype data provided by Rabbi et al (2020), and creates a file with NA written every time a phenotype is missing.

Next function creates a dataframe out of the results, and for each germplasm name, it takes an avarage of all phenotypic measures for that germplasm and does it for each trait
and creates a CSV-file.

Last function, takes the output (CSV) file as input and creates the correct format for the phenotype function. 


Pheno:file:
Family ID
Individual ID
Phenotype A
Phenotype B
Phenotype C
Phenotype D
Phenotype E..."""

#39 - 57 phenotypes
#Because of 2 commas in 

#Header = ["FID, IID, apical pubescence visual rating 0-2, mean green mite severity, mean_CMD_severity,central leaf shape visual rating 1-10,dry matter content percentage, 6first fully expanded leaf color visual rating 1-9, 7harvest index variable, 8petiole color visual rating 1-9, 9plant architecture visual rating 1-5, stem color visual scoring 1-4, 11storage root cortex color visual rating 1-4, storage root periderm color visual rating 1-4, total carotenoid by chart 1-8, unexpanded apical leaf color visual rating 1-9 ]
import statistics
import sys
def pheno(phenofile, output_phen, phenofile_guide):  #def function
    count_id = 0
    header2 = []  #append headers
    header = []
    cluster = []
    In_ID = []
    apical_pubescence_visual_rating = []
    mean_CGM_severity40_41 = []
    cassava_mosaic_disease_severity42_44 = []
    central_leaf_shape_visual_rating = []
    dry_matter = []
    leaf_color_visual_rating = []
    harvest_index = []
    petiole_color_visual_rating = []
    plant_architecture = []
    stem_color = []
    storage_root_color = []
    storage_root_periderm_color = []
    total_carotenoid = []
    unexpanded_apical_leaf_color_visual_rating = []
    header1 = ["FID","IID"]

    fh_pheno = open(phenofile, "r")  #input file with phenotype information
    for vi, line in enumerate(fh_pheno):  #go through file
        templine = line.rstrip('\n').split("\t")  #split by tab
        if vi == 0:  #store the header information
                
            header2.append(templine[39:55])
            header = header1 + header2
            print(header)
        if vi > 0:
            if templine[18] == "":
                templine[18] = templine[18].replace('','NA')
            In_ID.append(templine[18])
            if templine[39] == "":
                templine[39] = templine[39].replace('','NA')
            elif templine[39] == "0":
                templine[39] = templine[39].replace('0','0.0')
            elif templine[39] == "1":
                templine[39] = templine[39].replace('1','1.0')    
            elif templine[39] == "2":
                templine[39] = templine[39].replace('2','2.0')
            apical_pubescence_visual_rating.append(templine[39])
            
            tempsum_M = 0
            tempcount_M = 0 
            for item in templine[40:42]:
                item = item.replace(',', '.')
                if not item == "":
                    tempsum_M += float(item)
                    tempcount_M += 1 
            if tempcount_M == 0:
                M = "NA"
            else:
                M = str(tempsum_M/tempcount_M)
            mean_CGM_severity40_41.append(M.replace('.',','))
            
            tempsum_CMD = 0
            tempcount_CMD = 0 
            for item in templine[42:45]:
                item = item.replace(',', '.')
                if not item == "":
                    tempsum_CMD += float(item)
                    tempcount_CMD += 1 
            if tempcount_CMD == 0:
                CMD = "NA"
            else:
                CMD = str(tempsum_CMD/tempcount_CMD)
            cassava_mosaic_disease_severity42_44.append(CMD.replace('.',','))
            
            if templine[45] == "":
                templine[45] = templine[45].replace('','NA')
            elif templine[45] == "0":
                templine[45] = templine[45].replace('0','0.0')
            elif templine[45] == "1":
                templine[45] = templine[45].replace('1','1.0')    
            elif templine[45] == "2":
                templine[45] = templine[45].replace('2','2.0')
            central_leaf_shape_visual_rating.append(templine[45])
            if templine[46] == "":
                templine[46] = templine[46].replace('','NA')
            elif templine[46] == "0":
                templine[46] = templine[46].replace('0','0.0')
            elif templine[46] == "1":
                templine[46] = templine[46].replace('1','1.0')    
            elif templine[46] == "2":
                templine[46] = templine[46].replace('2','2.0')
            dry_matter.append(templine[46])
            if templine[47] == "":
                templine[47] = templine[47].replace('','NA')
            elif templine[47] == "0":
                templine[47] = templine[47].replace('0','0.0')
            elif templine[47] == "1":
                templine[47] = templine[47].replace('1','1.0')    
            elif templine[47] == "2":
                templine[47] = templine[47].replace('2','2.0')
            leaf_color_visual_rating.append(templine[47])
            if templine[48] == "":
                templine[48] = templine[48].replace('','NA')
            elif templine[48] == "0":
                templine[48] = templine[48].replace('0','0.0')
            elif templine[48] == "1":
                templine[48] = templine[48].replace('1','1.0')    
            elif templine[48] == "2":
                templine[48] = templine[48].replace('2','2.0')
            harvest_index.append(templine[48])
            if templine[49] == "":
                templine[49] = templine[49].replace('','NA')
            elif templine[49] == "0":
                templine[49] = templine[49].replace('0','0.0')
            elif templine[49] == "1":
                templine[49] = templine[49].replace('1','1.0')    
            elif templine[49] == "2":
                templine[49] = templine[49].replace('2','2.0')
            petiole_color_visual_rating.append(templine[49])
            if templine[50] == "":
                templine[50] = templine[50].replace('','NA')
            elif templine[50] == "0":
                templine[50] = templine[50].replace('0','0.0')
            elif templine[50] == "1":
                templine[50] = templine[50].replace('1','1.0')    
            elif templine[50] == "2":
                templine[50] = templine[50].replace('2','2.0')
            plant_architecture.append(templine[50])
            if templine[51] == "":
                templine[51] = templine[51].replace('','NA')
            elif templine[51] == "0":
                templine[51] = templine[51].replace('0','0.0')
            elif templine[51] == "1":
                templine[51] = templine[51].replace('1','1.0')    
            elif templine[51] == "2":
                templine[51] = templine[51].replace('2','2.0')
            stem_color.append(templine[51])
            if templine[52] == "":
                templine[52] = templine[52].replace('','NA')
            elif templine[52] == "0":
                templine[52] = templine[52].replace('0','0.0')
            elif templine[52] == "1":
                templine[52] = templine[52].replace('1','1.0')    
            elif templine[52] == "2":
                templine[52] = templine[52].replace('2','2.0')
            storage_root_color.append(templine[52])
            if templine[53] == "":
                templine[53] = templine[53].replace('','NA')
            elif templine[53] == "0":
                templine[53] = templine[53].replace('0','0.0')
            elif templine[53] == "1":
                templine[53] = templine[53].replace('1','1.0')    
            elif templine[53] == "2":
                templine[53] = templine[53].replace('2','2.0')
            storage_root_periderm_color.append(templine[53])
            if templine[54] == "":
                templine[54] = templine[54].replace('','NA')
            elif templine[54] == "0":
                templine[54] = templine[54].replace('0','0.0')
            elif templine[54] == "1":
                templine[54] = templine[54].replace('1','1.0')    
            elif templine[54] == "2":
                templine[54] = templine[54].replace('2','2.0')
            total_carotenoid.append(templine[54])
            if templine[55] == "":
                templine[55] = templine[55].replace('','NA')
            elif templine[55] == "0":
                templine[55] = templine[55].replace('0','0.0')
            elif templine[55] == "1":
                templine[55] = templine[55].replace('1','1.0')    
            elif templine[55] == "2":
                templine[55] = templine[55].replace('2','2.0')
            unexpanded_apical_leaf_color_visual_rating.append(templine[55])
        
            
                


 
    fh_out_phen = open(output_phen, "w")  #output file

    fh_phenofile_guide = open(phenofile_guide, 'r')  #open file with different ID-names
    for vi_phen_g, line_phen_g in enumerate(fh_phenofile_guide):  #go through it
        if vi_phen_g > 2:  #skip first 3 lines
            temp_line_pheno=line_phen_g.strip().split('\t')  #split by tab
            for vi_phen, item_phen in enumerate(In_ID):
                if item_phen == temp_line_pheno[3]:  #if the name from the ID-guide file is present in the phenotype guide-file
                    #print(In_ID)
                    fh_out_phen.write(temp_line_pheno[6]+ '\t' + item_phen + '\t' + apical_pubescence_visual_rating[vi_phen] + '\t' + mean_CGM_severity40_41[vi_phen] +'\t' + cassava_mosaic_disease_severity42_44[vi_phen] +'\t'+  central_leaf_shape_visual_rating[vi_phen] + '\t'+  dry_matter[vi_phen] + '\t'+  leaf_color_visual_rating[vi_phen] + '\t'+  harvest_index[vi_phen] + '\t'+  petiole_color_visual_rating[vi_phen] + '\t'+  plant_architecture[vi_phen] + '\t' +  stem_color[vi_phen]+ '\t' +  storage_root_color[vi_phen]+ '\t' +  storage_root_periderm_color[vi_phen]+ '\t' +  total_carotenoid[vi_phen] + '\t' +  unexpanded_apical_leaf_color_visual_rating[vi_phen])
                    fh_out_phen.write('\n')
                    
                        
                    #Missing phenotypes are always represented by the --[output-]missing-phenotype value (this is a very minor change from PLINK 1.07).
                    #ISSUE: take the mean of the strings and don't add them all together the strings, solution: do something with the "" but what?
    print(count_id)
    fh_phenofile_guide.close()
    fh_pheno.close()
    fh_out_phen.close()
    return 0 
phenofile_guide = "data_phenotype_guide.txt"
output_phen = "my_pheno_file.txt"
phenofile = "phenotype_file_p_t.txt"
pheno(phenofile, output_phen, phenofile_guide)



import pandas as pd
import numpy as np
def Make_pheno_2(phenotype_file, output_file):
    fh_in_pheno = open(phenotype_file, "r")
    #fh_out_pheno = open(output_file, "w")
    cluster = []
    In_ID = []
    apical_pubescence = []
    mean_CMD_severity40_41 = []
    cassava_green_mite_severity42_44 = []
    central_leaf_shape_visual_rating = []
    dry_matter = []
    leaf_color_visual_rating = []
    harvest_index = []
    petiole_color_visual_rating = []
    plant_architecture = []
    stem_color = []
    storage_root_color = []
    storage_root_periderm_color = []
    total_carotenoid = []
    Unexpanded_leaf_color = []
    empty = []
    dft = {}


    for vi, item in enumerate(fh_in_pheno):
        new_item = item.strip().split('\t')
        cluster.append(new_item[0])
        In_ID.append(new_item[1])
        apical_pubescence.append(new_item[2])
        mean_CMD_severity40_41.append(new_item[3])
        cassava_green_mite_severity42_44.append(new_item[4])
        central_leaf_shape_visual_rating.append(new_item[5])
        dry_matter.append(new_item[6])
        leaf_color_visual_rating.append(new_item[7])
        harvest_index.append(new_item[8])
        petiole_color_visual_rating.append(new_item[9])
        plant_architecture.append(new_item[10])
        stem_color.append(new_item[11])
        storage_root_color.append(new_item[12])
        storage_root_periderm_color.append(new_item[13])
        total_carotenoid.append(new_item[14])
        Unexpanded_leaf_color.append(new_item[15])
        

        
        
    df = {"Cluster": cluster, "ID": In_ID, "apical_pubescence_visual_rating": apical_pubescence,
              "mean_CMD_severity": mean_CMD_severity40_41, "cassava_green_mite" : cassava_green_mite_severity42_44, 
              "central_leaf_shape": central_leaf_shape_visual_rating, "dry_matter": dry_matter, 
              "leaf_color_visual_rating": leaf_color_visual_rating, "harvest_index" : harvest_index, 
              "petiole_color_visual_rating": petiole_color_visual_rating, "plant_architecture" : plant_architecture,
              "stem_color" : stem_color, 
              "storage_root_color" : storage_root_color, "storage_root_periderm_color" : storage_root_periderm_color,
              "total_carotenoid" : total_carotenoid, "Unexpanded_leaf_color" : Unexpanded_leaf_color}
   
    dft = pd.DataFrame(df, columns = ["Cluster", "ID", "apical_pubescence_visual_rating",
          "mean_CMD_severity", "cassava_green_mite", 
          "central_leaf_shape", "dry_matter", 
          "leaf_color_visual_rating", "harvest_index", 
          "petiole_color_visual_rating", "plant_architecture",
          "stem_color", 
          "storage_root_color", "storage_root_periderm_color",
          "total_carotenoid", "Unexpanded_leaf_color"], dtype = float)
    
    #dft.groupby(["Cluster"]).mean(
    newdf = dft.groupby(["Cluster","ID"], as_index=False)["apical_pubescence_visual_rating",
          "mean_CMD_severity", "cassava_green_mite", 
          "central_leaf_shape", "dry_matter", 
          "leaf_color_visual_rating", "harvest_index", 
          "petiole_color_visual_rating", "plant_architecture",
          "stem_color", 
          "storage_root_color", "storage_root_periderm_color",
          "total_carotenoid", "Unexpanded_leaf_color"].mean()
    

    fh_in_pheno.close()
    
    
    print(newdf)
    return newdf

phenotype_file = "my_pheno_file.txt"
output_file = "pheno_input.csv"
newdf = Make_pheno_2(phenotype_file, output_file)

newdf.to_csv(output_file, sep='\t', na_rep = "NA", header = False, index = False)
        


def make_file(input1, output1):
    fh_in_pheno2 = open(input1, "r")
    fh_out_pheno2 = open(output1, "w")
    for item2 in fh_in_pheno2:

        new_item = item2.strip().split('\t')
        #print(new_item[15])
        fh_out_pheno2.write(new_item[0] + '\t' + new_item[1] + '\t' + new_item[2] + '\t' + new_item[3] + '\t' + new_item[4] + '\t' + new_item[5] + '\t' + new_item[6] + '\t' + new_item[7] + '\t' + new_item[8] + '\t' + new_item[9] + '\t' + new_item[10] + '\t' + new_item[11] + '\t' + new_item[12] + '\t' + new_item[13] + '\t' + new_item[14] + '\t' + new_item[15])
        fh_out_pheno2.write('\n')
    fh_out_pheno2.close()
    return 0

input1 = "pheno_input.csv"
output1 = "Phenofile_1_6_2021.phen"
make_file(input1, output1)
    
    
    



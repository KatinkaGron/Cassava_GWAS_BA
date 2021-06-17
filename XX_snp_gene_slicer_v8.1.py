#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:02:38 2021

@author: katinka
"""

"""
This code takes the GCTA output (mlmi or mlme files), and creates an excel file with the top 20 most significant markers,
and the 10 genes that has the sortest distance to each SNP

It also creates an Manhattan plot and a corrosponding qq plot

Insert also a "name" for the correct file name (input below)

"""

## function that takes in the GWAS output and gives the top 5 p_values into a dataframe with position, ID, chromosome and p-value
## Between mlmi and mlme in each trait
import pandas as pd
import numpy as np
import os
#os.chdir("/Users/katinka/gcta_1.93.2beta_mac/V8_Pruned")
def find_genes(File_mlmi, file_mlme):
    fh_inv6 = open(File_mlmi, "r")
    list_of_top_SNPs6 = []
    list_of_top_SNPs7 = []
    CHR6 = []
    basepair6 = []
    p_value6 = []
    SNP6 = []
    df6 = {}

    
    for vi, item in enumerate(fh_inv6):
        if vi > 0:
            new_column = item.rstrip('\n').split('\t')
            CHR6.append(new_column[0])
            basepair6.append(new_column[2])
            p_value6.append(float(new_column[8]))
            SNP6.append(new_column[1])

    d6 = {"CHR":CHR6, "BP": basepair6, "P": p_value6, "SNP": SNP6}
    df6 = pd.DataFrame(d6, columns = ["CHR", "BP", "P", "SNP"])
    
    
    
    fh_inv7 = open(file_mlme, "r")
    CHR7 = []
    basepair7 = []
    p_value7 = []
    SNP7 = []
    df7 = {}

    
    for vi, item in enumerate(fh_inv7):
        if vi > 0:
            new_column = item.rstrip('\n').split('\t')
            CHR7.append(new_column[0])
            basepair7.append(new_column[2])
            p_value7.append(float(new_column[8]))
            SNP7.append(new_column[1])

    d7 = {"CHR":CHR7, "BP": basepair7, "P": p_value7, "SNP": SNP7}
    df7 = pd.DataFrame(d7)
    #print(df7)
    
    top_10_s6 = df6.sort_values(by=['P']).head(20)

    top_10_s7 = df7.sort_values(by=['P']).head(20)
    list_of_top_SNPs6 = top_10_s6.values.tolist()

    list_of_top_SNPs7 = top_10_s7.values.tolist()
    fh_inv6.close()
    fh_inv7.close()
    return list_of_top_SNPs6, list_of_top_SNPs7

## writes top5 p-value sorted dataframes into lists
name = "Apical_Pubescence"
file_mlme = "Apical_pubescence_new/Apical_pubescence_v8_mlme.loco.mlma"
File_mlmi = "Apical_pubescence_new/Apical_pubescence_v8_mlmi.mlma"




find_genes(File_mlmi, file_mlme)
import pandas as pd
def surrounding_genes(annotationsv6, annotationsv7):
    list_of_top_SNPs6, list_of_top_SNPs7 = find_genes(File_mlmi, file_mlme)
    fh_v6 = open(annotationsv6, "r")
    list_of_GENES6 = []
    G_name = []
    Chr = []
    direction = []
    b_start = []
    b_end = []
    b_middle = []
    df6 = {}
    sc = "Scaffold"
    for vi, item in enumerate(fh_v6):
        if vi > 0:
            if sc not in item:
                temp_line = item.rstrip('\n').split('\t')
                G_name.append(temp_line[0])
                if temp_line[2].startswith("Chromosome0"):
                    temp_line[2] = temp_line[2].lstrip("Chromosome0")
                elif temp_line[2].startswith("Chromosome"):
                    temp_line[2] = temp_line[2].lstrip("Chromosome")
                Chr.append(int(temp_line[2]))
                direction.append(int(temp_line[3]))
                b_start.append(temp_line[4])
                b_end.append(temp_line[5])
                b_middle.append(int(temp_line[5])-((int(temp_line[5])-int(temp_line[4]))/2))
            
    d6 = {"Gene_name": G_name, "Chromosome": Chr, "Direction": direction, "bp_start": b_start, "bp_end" : b_end, "b_middle" : b_middle}
    df6 = pd.DataFrame(d6, columns= ['Gene_name','Chromosome', "Direction", "bp_start", "bp_end", "b_middle" ])
    #harvest_index6 = df6.sort_values(by=['Chromosome'])
    harvest_index6 = df6.sort_values(by=['Chromosome','Direction', "b_middle"]).drop_duplicates(subset='Gene_name', keep= 'last')
    list_of_GENES6 = harvest_index6.values.tolist()
    #print(top_10_s6)

    #print(list_of_top_SNPs6)
    #print(list_of_GENES6[1:10])
    big_number = 1000000000
    list_of_genes = []
    for vi, item_top in enumerate(list_of_top_SNPs6):
        dist_to_marker = []
        for vl, item_genes in enumerate(list_of_GENES6):
            if item_top[0] == str(item_genes[1]):
                result = abs(int(item_top[1]) - int(item_genes[5]))
                dist_to_marker.append(result)        
            else:
                dist_to_marker.append(big_number)
    
    
        sorted_index = sorted(range(len(dist_to_marker)), key = dist_to_marker.__getitem__)
        #print(sorted_index)
        #print(list_of_GENES6[sorted_index[:10]])
        for vi in range(10):
            #print(sorted_index[vi])
            #print(list_of_GENES6[sorted_index[vi]])
            list_of_genes.append(list_of_GENES6[sorted_index[vi]])
            
    #write to excel
            
    fh_v6.close()
            
    fh_v7 = open(annotationsv7, "r")
    list_of_GENES7 = []
    G_name7 = []
    Chr7 = []
    direction7 = []
    b_start7 = []
    b_end7 = []
    b_middle7 = []
    df7 = {}
    sc = "Scaffold"
    for vi, item in enumerate(fh_v7):
        if vi > 0:
            if sc not in item:
                temp_line = item.rstrip('\n').split('\t')
                G_name7.append(temp_line[0])
                if temp_line[2].startswith("Chromosome0"):
                    temp_line[2] = temp_line[2].lstrip("Chromosome0")
                elif temp_line[2].startswith("Chromosome"):
                    temp_line[2] = temp_line[2].lstrip("Chromosome")
                Chr7.append(int(temp_line[2]))
                direction7.append(int(temp_line[3]))
                b_start7.append(temp_line[4])
                b_end7.append(temp_line[5])
                b_middle7.append(int(temp_line[5])-((int(temp_line[5])-int(temp_line[4]))/2))
            
    d7 = {"Gene_name": G_name7, "Chromosome": Chr7, "Direction": direction7, "bp_start": b_start7, "bp_end" : b_end7, "b_middle" : b_middle7}
    df7 = pd.DataFrame(d7, columns= ['Gene_name','Chromosome', "Direction", "bp_start", "bp_end", "b_middle" ])
    #harvest_index6 = df6.sort_values(by=['Chromosome'])
    harvest_index7 = df7.sort_values(by=['Chromosome','Direction', "b_middle"]).drop_duplicates(subset= 'Gene_name', keep= 'last')
    list_of_GENES7 = harvest_index7.values.tolist()
    #print(list_of_GENES6)

    #print(list_of_top_SNPs6)
    #print(list_of_GENES6[1:10])
    big_number = 1000000000
    list_of_genes7 = []
    for vi, item_top in enumerate(list_of_top_SNPs7):
        dist_to_marker7 = []
        for vl, item_genes in enumerate(list_of_GENES7):
            if item_top[0] == str(item_genes[1]):
                result = abs(int(item_top[1]) - int(item_genes[5]))
                dist_to_marker7.append(result)        
            else:
                dist_to_marker7.append(big_number)
    
    
        sorted_index = sorted(range(len(dist_to_marker7)), key = dist_to_marker7.__getitem__)
        #print(sorted_index)
        #print(list_of_GENES6[sorted_index[:10]])
        for vi in range(10):
            #print(sorted_index[vi])
            #print(list_of_GENES6[sorted_index[vi]])
            list_of_genes7.append(list_of_GENES7[sorted_index[vi]])
            
            #write to excel 
    
    df_lgenes7 = pd.DataFrame(list_of_genes7, columns= ['Gene_name','Chromosome', "Direction", "bp_start", "bp_end", "b_middle" ])
    df_lgenes6 = pd.DataFrame(list_of_genes, columns= ['Gene_name','Chromosome', "Direction", "bp_start", "bp_end", "b_middle" ])



    
    fh_v7.close()

    new_list1 = list_of_top_SNPs6
    new_list2 = list_of_top_SNPs7
    df1 = pd.DataFrame(new_list1)
    df2 = pd.DataFrame(new_list2)
    writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
    df1.to_excel(writer, sheet_name='list_of_top_SNPs6_MLMI', index=False)
    df2.to_excel(writer, sheet_name='list_of_top_SNPs6_MLMe', index=False)
    df_lgenes6.to_excel(writer, sheet_name='100_genes6_MLMI', index=False)
    df_lgenes7.to_excel(writer, sheet_name='100_genes6_MLMe', index=False)
    writer.save()

    return 0

annotationsv6 = "mart_export_v8.txt"
annotationsv7 = "mart_export_v8.txt"
surrounding_genes(annotationsv6, annotationsv7)


import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
def makeManhatten(file_mlme, File_mlmi):
    fh_in = open(file_mlme, "r")
    CHR = []
    basepair = []
    p_value = []
    SNP = []
    df = {}
    
    for vi, item in enumerate(fh_in):
        if vi > 0:
            new_column = item.rstrip('\n').split('\t')
            CHR.append(new_column[0])
            basepair.append(new_column[2])
            p_value.append(float(new_column[8]))
            SNP.append(new_column[1])

    d = {"CHR":CHR, "BP": basepair, "P": p_value, "SNP": SNP}
    df = pd.DataFrame(d)
    

    
    #print(p_value)
    fh_in.close()
        
    fh_in_wo = open(File_mlmi, "r")
    CHRwo = []
    basepairwo = []
    p_valuewo = []
    SNPwo = []
    df_wo = {}
    
    for vi, item in enumerate(fh_in_wo):
        if vi > 0:
            new_columnwo = item.rstrip('\n').split('\t')
            CHRwo.append(new_columnwo[0])
            basepairwo.append(new_columnwo[2])
            p_valuewo.append(float(new_columnwo[8]))
            SNPwo.append(new_columnwo[1])

    d = {"CHR":CHRwo, "BP": basepairwo, "P": p_valuewo, "SNP": SNPwo}
    df_wo = pd.DataFrame(d)


    fh_in_wo.close()
    return df, df_wo


df, df_wo = makeManhatten(file_mlme, File_mlmi)
#print(df)

from qqman import qqman
import pandas as pd
import matplotlib.pyplot as plt

from qqman import qqman
qqman.manhattan(df, out="manhatten_" + name + "_LOCO.png", title="Manhattan V8 - " + name + "LOCO")
qqman.qqplot(df, out="qq_" + name + "LOCO.png", title="QQ-plot V8 - " + name)

qqman.manhattan(df_wo, out="manhatten_" + name + ".png", title="ManhattanV8 - " + name)
qqman.qqplot(df_wo, out="qq_" + name + ".png", title="QQ-plot V8 - " + name)





 

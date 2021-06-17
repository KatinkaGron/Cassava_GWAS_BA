#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:09:51 2021

@author: katinka
"""
"""

Removing duplicate lines and keeps one of them, targeted the markers that are duplicated allignments within 100 kb
**this function sometimes failes, remember to count amount of duplicates before and removed after!


"""

import pandas as pd

def remove_duplicates_in_map(MAP_From_create_MAP, Finished_MAP):
    whole_map = []
    CHR = []
    SNP_ID = []
    zero = []
    pos = []
    fh_in_MAP = open(MAP_From_create_MAP, "r")
    for item in fh_in_MAP:
        temp_item = item.rstrip('\n').split('\t')
        CHR.append(temp_item[0])
        SNP_ID.append(temp_item[1])
        zero.append(temp_item[2])
        pos.append(temp_item[3])
    dataframe1 = pd.DataFrame({'CHR': CHR,'SNP_ID': SNP_ID, "zero": zero, "position": pos })
    df2 = dataframe1.drop_duplicates(subset= 'SNP_ID', keep= 'last')
    
    whole_map = df2.values.tolist()
    
    fh_map = open(Finished_MAP, "w")
    for LN, subList in enumerate(whole_map):
        for item in subList:
            if LN == 0:
                fh_map.write(item + "\t")
            else:
                fh_map.write(item + "\t")
        
        fh_map.write("\n")
    
    fh_map.close()
    
    return 0
MAP_From_create_MAP = "Map_w_duplicates.tsv"
Finished_MAP = "MAP_finish_wo_duplicates_v7.map"
remove_duplicates_in_map(MAP_From_create_MAP, Finished_MAP)

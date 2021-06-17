#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:58:31 2021

@author: katinka
"""
"""
This file takes the VCF-file as an input and transposes it, to make it suitable for creating the PED file.
(High computational load)

"""


def transpose_vcf(vcf, transposed_vcf):
    fh_dummy_vcf = open(vcf, "r")
    
    container = []

    
    warning = False
    for vl, line in enumerate(fh_dummy_vcf):
        if vl % 10000 == 0: 
            print("reading in " + str(vl))
        if line.startswith('##'):
            if warning:
                print("ignore header line")
        elif line.startswith('#'):
            container.append(line.strip().lstrip("#").split('\t'))    
        else:
            container.append(line.strip().split('\t'))

    fh_dummy_vcf.close()
    print("transposing")
    try:
        fh_transposed = open(transposed_vcf, "w")
    except IOError:
        print("can't open file")
    for vi in range(len(container[0])):
        for vj in range(len(container)):
            #if vj % 10000 == 0:
            print("writing " + str(vj))
            if vj == 0:
                fh_transposed.write(container[vj][vi])
            else:
                fh_transposed.write("\t" + container[vj][vi])
        fh_transposed.write("\n")
    fh_transposed.close()
    return 0

#vcf = "transposed_vcf.tsv"
#transposed_vcf = "dummy_vcf.vcf"     
#fh_transposed = transpose_vcf(dummy_vcf,transpose_dummy_vcf)
#print(fh_transposed)

  # next section: Run from terminal:

  
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
        transpose_vcf(sys.argv[1],sys.argv[2])







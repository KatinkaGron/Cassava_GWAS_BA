#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:38:38 2021

@author: katinka
"""

"""
PART 1

The purpose of the first part of the script, is to take the VCF file, and create 3 files, which containes information about:


1. SNP_chr = "Chromosome_number.txt" (Chromosome number)
2. SNP_pos = "bp_position.txt" (Marker positions in bp)
3. chr_ID = "ID.txt" (Marker ID's)

"""



#input is the VCF file, output sliced 3 files in ID's, CHROM_number and bpPosition'
def sort_vcf(file):
    Chrom5 = []
    POS5 = []
    ID5 = []
    Header =["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT"]
    with open(file, "r") as fh:
        for line in fh:
            if not line.startswith('#'):
                temp_line1=line.strip().split('\t')
                Chrom5.append(temp_line1[0])
                POS5.append(temp_line1[1])
                ID5.append(temp_line1[2])   
    fh.close()
    return Chrom5, POS5, ID5


file ="Rabbi_GWAS.vcf"
Chrom5, POS5, ID5 = sort_vcf(file)
with open ("Chromosome_number.txt", "w") as Chrom:
    for item in Chrom5:    
        print(item, file=Chrom)
    Chrom.close()
with open ("bp_position.txt", "w") as POS:
    for item2 in POS5:
        print(item2, file=POS)
    POS.close()
with open ("ID.txt", "w") as ID:
    for itemID in ID5:
        print(itemID, file=ID)
    ID.close()


"""
PART 2

Function that takes a reference genome, and process it to the relevant format for part 3. The purpose is to divide the header information of each chromosome
and each sequence belonging to that chromosome, into lists that follow the same linenumber, to access them later. 

"""

def create_seq(file):  #This function takes a fasta file and returns 2 lists, 1 with the sequences (each line = sequence of entire chromosome), and 1 with the corrosponding headers + removing linebreaks 
    status_lines = []  # List where the headers is added
    sequences_v6 = []  # List where the sequence is added
    is_not_first_seq = False  
    fh = open(file, "r")
    for line in fh:  # go through the fasta file line by line, and remove line characters every time i see a ">" I remove it, and add the header to statuslines
        line = line.rstrip()  
        if line.startswith(">"):  
            last_status = line 
            status_lines.append(last_status.lstrip(">"))
            if is_not_first_seq == True :  #this makes sure that we get more than just the first title and go through the entire docuement.
                sequences_v6.append(temp_sequence) #We append the sequnces to temp_sequence folder
            temp_sequence = ""   
            is_not_first_seq = True    
        else:
            temp_sequence += "".join(line.split()) #splitting the sequences into seperate arrays, and joining them into the list temp sequneces
    sequences_v6.append(temp_sequence) # sequences_v6 we compine the temp_sequence, outside the loop to include the last line
    fh.close()

    return sequences_v6, status_lines  #return of the function
#file = "Mesculenta_305_v6.fa"
#sequences_v6, status_lines = create_seq(file)
#print(status_lines[0])
#print(sequences_v6[0][0:100])

    

def fun_CHR_NAME(status_lines, file): #This function edits the results create_seq(file). It removes the initial part of the title and returns only the number, since this is needed to compare lines later
    CHR_NAME = []  #return list of CHR_NAMEs
    sequences_v6, status_lines = create_seq(file)  #call prev. function
    for line in status_lines:  #go through the headers line by line and if they start with Chromosome0, we remove and add the rest to the list
        if line.startswith("Chromosome0"):
            CHR1_9 = line
            CHR_NAME.append(CHR1_9.lstrip("Chromosome0"))
        elif line.startswith("Chromosome"):  #go through the headers line by line and if they start with Chromosome, we remove and add the rest to the list
            CHR10_18 = line
            CHR_NAME.append(CHR10_18.lstrip("Chromosome"))
    return CHR_NAME  #list of chromosome numbers
#CHR_NAME = fun_CHR_NAME(status_lines)  #call outside function.
#print(CHR_NAME)
#print(CHR_NAME)


SNP_chr = "Chromosome_number.txt"
SNP_pos = "bp_position.txt"
chr_ID = "ID.txt"
file = "Mesculenta_305_v6.fa"   #read files

"""
PART 3

Function that takes the processed sequences + Headers from the fasta files (before), and uses the SNP-position information on chromosome number and bp position from the VCF-file,
to lokate the SNP's on the genome, and in return writes a file with 151 bp sequence, from 75 bp up-and downstream from each SNP.

"""

def find_position(SNP_chr, SNP_pos, chr_ID, N_of_bp, file):
    sequences_v6, status_lines = create_seq(file)  #calling functions from above
    CHR_NAME = fun_CHR_NAME(status_lines, file)  #calling functions from above
    SNP_sequences = []  #list where the 75 bp SNP sequences are added to
    id_list = []
    fh_SNP_chr = open(SNP_chr, "r")  #Open SNP_chromosome positions (chromosome number)
    #print(status_lines[0:10],CHR_NAME[0:10])
    for LN_SNP_chr, line_SNP_chr in enumerate(fh_SNP_chr):  #go through the file line by line
        #print(line_SNP_chr)    
        found_it = False
        line_SNP_chr_stripped = line_SNP_chr.rstrip()
        for LN_CHR_NAME, line_CHR_NAME in enumerate(CHR_NAME):  #go through the processed Sequence_chromosome_header file line by line
            if line_SNP_chr_stripped == line_CHR_NAME:  #if the chromosome number is the same the continue
                for LN_sequence, line_sequence in enumerate(sequences_v6):  #go through the sequences line by line
                    if LN_sequence == LN_CHR_NAME:  #if the line number of the sequences and the header files are equal then store the sequence in the temp. folder store_sequence2
                        store_sequence2 = line_sequence
                        found_it = True
                        break
                        
                if found_it:
                    break 
        fh_SNP_pos = open(SNP_pos, "r")  # open SNP bp position file
        for LN_SNP_pos, line_SNP_pos in enumerate(fh_SNP_pos):  #go through the file line by line
            line_SNP_pos2 = line_SNP_pos.rstrip() 
            if LN_SNP_pos == LN_SNP_chr:  #if the LN of the SNP position and the SNP chromosome number is the same then:
                SNP_sequences.append(store_sequence2[int(line_SNP_pos2)-1-N_of_bp:int(line_SNP_pos)+N_of_bp]) #now we insert into SNP_sequences= we go into the temp_stored_sequences, and for each bp position line, we go 75+ and 75- nt up and downstram each SNP position and insert the sequence into SNP_sequences
    fh_SNP_chr.close()  #close files
    fh_SNP_pos.close()
    with open (chr_ID, "r") as Chromosome_id_file: #open chr ID files
        for ID_item in Chromosome_id_file:  #iterate
            stripped_ID_item = ID_item.rstrip()  #remove linebreaks
            id_list.append(stripped_ID_item)  #append to id_list of seq ID's
    with open ("SNP_sequences.fa", "w") as SNP_SEQ_file:  #open sequence file
        for VI, item in enumerate(SNP_sequences):  #enumerate over list of sequences
            print(">",id_list[VI], file=SNP_SEQ_file)  #start every line with > for a fasta format, use the line number of seq ID for correcte seperation, create file of SNP.sequences where each sequence is seperated by a line break
            print(item, file=SNP_SEQ_file)
    SNP_SEQ_file.close()
    return SNP_sequences  #return the sliced products

 
#SNP_sequences = find_position(SNP_chr, SNP_pos, 75, "Mesculenta_305_v6.fa")  #call function

#print(SNP_sequence2) #print

"""
The output of the last function is a fasta file of SNP sequences can now be BLASTED onto the reference genome of interest

"""











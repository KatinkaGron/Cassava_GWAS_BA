# Code_for_GWAS_input_(Cassava_BA)


The codes includes a step by step procedure on how to produce MAP, PED and PHENO files from an excisting VCF file and the reference genome the VCF file was produced from. 

1. A VCF file and the reference genome it was made from is used to create small sequences related to each marker. The sequences consist of 75 basepairs sequences flanking each marker. In the end, a file is produced that consist of 151 bp-sequences and in each sequence the marker of interest is in the center. 
2. These sequences are then mapped onto a genome of choice using BLAST (procedure not described here, but can be found online).
3. The code then uses the BLAST results to produce the MAP and PED files, which are used as input files for the software PLINK 
4. PLINK is then used to produce the binary files from the MAP and PED files. 
5. The binary files can then be used for the software GCTA, which is used to perform the GWAS, in this step the Pheno type file is added. *Control which phenotype is tested with --mpheno [1-14]. 
6. This repository includes a code that provide Manhattan plots, QQ-plots and a table of the 20 most significant markers for each trait is included 


"""

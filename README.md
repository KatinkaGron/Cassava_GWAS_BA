# Cassava_GWAS_BA

"""
The codes describe a step by step procedure, on how to produce MAP, PED and pheno files from an excisting VCF file and the reference genome the VCF file was produced from. 

1. A VCF file and the reference genome it was made from, is used to create sequences, consisting of 75 basepairs sequences flanking each marker. In the end, a file is produced that consist of 151 BP-sequences, and in each sequence, the marker of interest is in the center. 
2. These sequences are then used to BLAST onto another genome of interest. 
3. The BLAST results are then used to produce the MAP and PED files, which are used as input files for PLINK 
4. Plink is then used to produce the binary files from the MAP and PED files. 
5. The binary files can then be used for GCTA, which was used to perform the GWAS, in this step the Pheno type file is added. *Control which phenotype is tested with --mpheno [1-14]
6. Code that provide Manhattan plots, QQ-plots and a table of the 20 most significant markers for each trait is included 


"""

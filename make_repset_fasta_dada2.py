#! /usr/bin/env python

# Date : 05th April 2019

# Author : Nirosh D. Aluthge

# INPUT : Two column tab-delimited file with first column having '>ASV_id' and second column with 'ASV sequence'

# OUTPUT : FASTA-formatted output file with ASV_id as header followed by corresponding sequence

import re 

taxa_table = open ("ASV_full_taxonomy_table.txt", "r")
output_fasta = open("ASV_rep_set.fasta", "w")

file_contents = taxa_table.readlines()

for line in file_contents :
	line = line.rstrip("\n")
	if not line.startswith('ASV_id') :
		line = line.split("\t")
		print(line[0])
		output_fasta.write('>' + line[0] + "\n" + line[1] + "\n")

output_fasta.close()

# The following commands will remove the empty line at the end of the earlier output and write to a new file

fasta_file = open("ASV_rep_set.fasta", "r")
data = fasta_file.read()

out_file = open("ASV_rep_set.fasta", "w")
out_file.write(data[:-1])

fasta_file.close()
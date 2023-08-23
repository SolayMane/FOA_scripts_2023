#!/usr/bin/env python3
# created on 03/12/2021
#author : Slimane Khayi, PhD 
# email :slimane.khayi@inra.ma
# this code is aiming to get fasta sequence from multifasta file using
#the matched headers in a file and appending new information on the headers 

import os
from Bio import SeqIO

pwd=os.getcwd()

#this is the output file that will contain all fasta sequences
output=open("cazymeGeneSeq.fasta","w")

# open the file all.fasta that contains all proteins from 19 fromae speciales FO
with open("all.fasta","r") as f:
  
        # read fasta file with biopython  
        myfastalist=list(SeqIO.parse(f,'fasta'))
        
        #we will create a dict of header and sequences because if we iterate over a fasta file to look for righ header this will take time
        dict={}
        
        # we go through fasta sequence and get the header and the seq in deparate variables
        for record in myfastalist:
                header=str(record.id)
                seq=str(record.seq)
                
                #stoore the heaeder and the sequence in a dic as key and value
                dict[header]=seq




#we will open the file with the liste of genes that we want to retrieve
with open("results","r") as cazID:
  
        #we iterate over the liste  
        for caz in cazID:
        
                #get the gene id         
                gene=caz.split("\t")[0]
            
                # get the cazyme info
                cazname=caz.split("\t")[2]
                
                # then if this gene id is in the prevously build dict, so we want to get his sequence
                if gene in dict:
                  
                        # we will write the sequence with the new header infromation to a file   
                        output.write(">"+str(gene)+"_"+str(cazname)+str(dict[gene])+"\n")
output.close()

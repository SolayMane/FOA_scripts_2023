# MCScanX analysis
Here you will find the procedure for assessing collinearity between two genome sequence using MCScanX tool
I will run the procedure for making McscnaX plot
1. First of all, run makeblastdb of the one of your proteins dataset. I'll use the proteins of Foa44 as a DB<br>
`makeblastdb -in old_run/mcscanX/Fusarium_oxysporum_f.sp._albedinis_Foa_44.proteins.fa -dbtype prot -out db/foa44`

2. Obtain the proteins sequences and transcripts from the gff file from ncbi because the proterins file in ncbi was not nicelly annotated<br>
````bash
gffread  -g GCA_023509805.1_Fusoxalb1_genomic.fna GCA_023509805.1_Fusoxalb1_genomic.gff \
-x strain9_Transcripts.fasta -y strain9_Proteins.fasta`
#I have to rename the proten fasta file keeping only the gene ID and renaming the full stop codon from . to *
cat ../strain9_assembly/densities/strain9_Proteins.fasta | awk '/>/ {print ">"$2} !/>/' | sed 's/gene=//g' | sed 's/\./*/g' > \
../strain9_assembly/densities/Clean_strain9_proteins.fasta
````
3. Look for the the query dataset FOA strain9, then run a blastp search
````bash
blastp -query ../strain9_assembly/densities/Clean_strain9_proteins.fasta -db db/foa44 -max_target_seqs 5 -evalue 0.0000000001 -num_threads 56 -outfmt 6 > xyz.blast
````
4. I need to generate a custom gff file using awk for both strains to include in the comparaison then contactenate those gff files in one
````bash
# the custom gff should have this form
  chr gene  start end
# This lie is for the strain9
````bash
awk -F"\t" '($3=="gene") { print $1,substr($9,9,17),$4,$5}' OFS='\t' \
../strain9_assembly/densities/GCA_023509805.1_Fusoxalb1_genomic.gff > strain9_custom.gff
````
# this is for Foa44
````bash
awk -F"\t" '($3=="gene") { print $1,substr($9,4,10)".t1",$4,$5}' OFS='\t' \
/sanhome2/data/FOA/Annotation_NRI/funannoate_new_run/annotate_results/Fusarium_oxysporum_f.sp._albedinis_Foa_44.gff3 \
> Foa44_custom.gff
````
# I had an issue with the custom gff file where I wanted to add ".t1" to the gene id at the fourth column I used awk
<code>awk -F "\t" '{ if ($4 ~ /^gene_/) { $4 = $4 ".t1" } print }' OFS='\t' xyz.gff > xyz1.gff</code>

5. Create a dir and mv all xyz.* file to it and run MCSCANX
MCScanX dir/xyz
5. Load the outputs (.collinearity File and .gff) into https://synvisio.github.io/#/


## Script in R to plot the genome sequence of Foa 44 
````R
library(karyoploteR)
library(GenomicRanges)
library(seqinr)


# read the genome file
seqs <- readDNAStringSet("Fusarium_Oxysporum.f.sp_albedinis_Foa44_scaffolds.fasta")

seqs

A DNAStringSet instance of length 51
       width seq                                            names
 [1] 6425555 ACCATCGGTCGTGCAGGTATGG...GATAACACTAGTTTGAGCTGC Chr_1
 [2] 4959882 GCCGATATGGTTGTTCTCGTCA...TGCTGCCTTCCTTGGATGTAG Chr_2
 [3] 5533475 GGCGATCCCAACGGGAATCGAG...TGCGGACCAGTTTACACTGTG Chr_4
 [4] 5216386 TTAAAACAAATTAAAAACAAAA...GCTGTTAAATCACCTGCCTGT Chr_5
 [5]  719069 TATATTTAGCCTTTATTTATTA...GTACTTAATAGGCAATATCAA Contig9
 ...     ... ...
[47]  559280 TGCCGAATGCCTTCCAAATCCT...GTCGAGCAGCCAGTTTCTGCG Contig62
[48]  762702 TGGTTATTATATAAATCATAGG...CAAGCCCATATCAAACCATGT Contig65
[49]   28777 ACACTGCAAATCCACGTGGACC...GGGTGTAATCTACAGAGGTAC Contig67
[50] 2224524 CGACTCATCCTCTAGTCGATTA...CTATTCTCGCCGAGCTCTACC Contig68
[51] 1101325 TCTTATAAAGCTTAATAAATAT...CGACTAGCTGATCCGCTTGCT Contig69

# show the names of the chromosomes :
names(seqs)
[1] "Chr_1"    "Chr_2"    "Chr_4"    "Chr_5"    "Contig9"  "Chr_7"
 [7] "Chr_8"    "Chr_9"    "Chr_10"   "Chr_11"   "Chr_12"   "Chr_13"
[13] "Contig4"  "Contig19" "Contig32" "Contig52" "Contig1"  "Contig3"
[19] "Contig7"  "Contig8"  "Contig11" "Contig12" "Contig15" "Contig17"
[25] "Contig18" "Contig20" "Contig21" "Contig22" "Contig23" "Contig24"
[31] "Contig25" "Contig26" "Contig29" "Contig31" "Contig33" "Contig34"
[37] "Contig36" "Contig38" "Contig42" "Contig46" "Contig49" "Contig50"
[43] "Contig51" "Contig54" "Contig56" "Contig59" "Contig62" "Contig65"
[49] "Contig67" "Contig68" "Contig69"

# show the length of evry chromosome
width(seqs)
[1] 6425555 4959882 5533475 5216386  719069 4524080 4061178 3585837 2988737
[10] 3366405 2470664 1939190  219773   98062  739887  253508 4552110  106397
[19]  348103  292509   16957 1460290  111937   52541   17615   11931 1075255
[28]  172767  416687 1447900  619460  176448   31891   31723  825899  392264
[37]  335227   49972  402445  209928  105261   31418   18547   55591  574674
[46]  249782  559280  762702   28777 2224524 1101325

# so we will use theses data to build a custom genome for our sequence using toGranges

custom.genome <- toGRanges(data.frame(chr=c(names(seqs)), start=c(1), end=c(width(seqs)))

# then we will plot the chromosome
 kp <- plotKaryotype(genome=custom.genome)

 ````
 
![image](https://user-images.githubusercontent.com/22656460/131832098-07adc51b-4a1c-4e5b-b039-0fc3502a2c5b.png)
 
 ````R
 # we will sort the labels based on chrom name
 kp <- plotKaryotype(genome=custom.genome, chromosomes = c(sort(names(seqs))), plot.type = 6)
 # orde the chrom based also on the length
 
 chr <-c("Chr_1","Chr_2","Chr_4","Chr_5","Chr_7","Chr_8",
 + "Chr_9","Chr_10","Chr_11","Chr_12","Chr_13",
 + "Contig1","Contig68","Contig12","Contig24",
 + "Contig69","Contig21","Contig33",
 + "Contig65","Contig32","Contig9",
 + "Contig25","Contig56","Contig62","Contig23",
 + "Contig42","Contig34","Contig7","Contig36","Contig8",
 + "Contig52","Contig59","Contig4","Contig46","Contig26",
 + "Contig22","Contig15","Contig3","Contig49","Contig19",
 + "Contig54","Contig17","Contig38","Contig29","Contig31",
 + "Contig50","Contig67","Contig51","Contig18",
 + "Contig11","Contig20")
 
 kp <- plotKaryotype(genome=custom.genome, chromosomes = chr, plot.type=6, cex=0.9)
 ````
 ![image](https://user-images.githubusercontent.com/22656460/131840702-eb37ef25-ba65-4f84-818e-fa7556cb59c0.png)


#  load a gene model from a GFF or GTF file
````R
library(GenomicFeatures)
txdb <- makeTxDbFromGFF("Fusarium_oxysporum_f.sp._albedinis_Foa_44.gff3", format ="gff3")
TxDb object:
# Db type: TxDb
# Supporting package: GenomicFeatures
# Data source: Fusarium_oxysporum_f.sp._albedinis_Foa_44.gff3
# Organism: NA
# Taxonomy ID: NA
# miRBase build ID: NA
# Genome: NA
# transcript_nrow: 20416
# exon_nrow: 55287
# cds_nrow: 54898
# Db created by: GenomicFeatures package from Bioconductor
# Creation time: 2021-09-02 14:43:25 +0000 (Thu, 02 Sep 2021)
# GenomicFeatures version at creation time: 1.38.2
# RSQLite version at creation time: 2.2.8
# DBSCHEMAVERSION: 1.2


# get genes
genes(txdb)

GRanges object with 1047 ranges and 1 metadata column:
          seqnames          ranges strand |     gene_id
             <Rle>       <IRanges>  <Rle> | <character>
    60S_1    Chr_4 3544693-3545396      - |       60S_1
    60S_2    Chr_9 1313008-1314052      - |       60S_2
  AAD14_1   Chr_11 2459485-2460627      + |     AAD14_1
  AAD14_2 Contig12   295082-296224      + |     AAD14_2
     AAH1    Chr_1 1018975-1020036      - |        AAH1
      ...      ...             ...    ... .         ...
     YTM1    Chr_5 3141105-3142850      + |        YTM1
   ZRA1_1    Chr_7 4019087-4024124      + |      ZRA1_1
   ZRA1_2    Chr_8   965844-970566      - |      ZRA1_2
   ZRA1_3   Chr_10   446669-451645      - |      ZRA1_3
   ZRA1_4   Chr_12 2320425-2325475      - |      ZRA1_4

all.genes <-genes(txdb)

### plot gene density
 kp <- kpPlotDensity(kp, all.genes, window.size =50000, data.panel=2)
 
 ## now, wil will compute the covrage through a mapping bam file and try to plot the covrage
 library(GenomicAlignments)
 bamfile <- readGAlignments("/disk1/FOA/SNP/foaSNP/FmodqC/snps.bam")
 covrage <- coverage(bamfile)
 kp <- plotKaryotype(genome=custom.genome, 
 + chromosomes = c("Chr_1","Chr_2","Chr_4","Chr_5","Chr_7","Chr_8","Chr_9","Chr_10","Chr_11","Chr_12","Chr_13","Contig1"),
 + plot.type =1,cex=0.9)
 kpPlotCoverage(kp, data=covrage, data.panel=2, col ="blue")

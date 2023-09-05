#!/bin/bash

# Set paths and filenames
ref_genome="ref.fa"
read1="/sanhome2/data/raw/Illumina/M13C_S2_L002_R1_001.fastq.gz"
read2="/sanhome2/data/raw/Illumina/M13C_S2_L002_R2_001.fastq.gz"
output_prefix="M13C_S2"

# Step 1: Map reads to the reference genome using BWA-MEM
bwa mem -t 56 "$ref_genome" "$read1" "$read2" > "${output_prefix}.sam"

# Step 2: Convert SAM to BAM and sort
samtools view -@ 4 -bS "${output_prefix}.sam" | samtools sort -@ 4 -o "${output_prefix}_sorted.bam"

# Step 3: Index the sorted BAM file
samtools index "${output_prefix}_sorted.bam"



bamtocov M13C_S2_sorted.bam -T 56 -Q 20 > essai.txt



RRRRR

library(table.data)

ref <- readDNAStringSet("ref.fa")
#  change headers of sequences to be shorter

genome <- toGRanges(data.frame(chr=c(names(ref)), start=1, end=c(width(ref))))

coverage_data <- fread("/sanhome2/Fusarium/CoverageAnalysis/test.txt", header = FALSE, col.names = c("Chromosome", "Start","End", "Coverage"))
pdf(file="coverage_vs_fol4287.pdf")

cv <- toGRanges(data.frame(chr=c(coverage_data$Chromosome), start=c(coverage_data$Start), end=c(coverage_data$End), Cov=c(coverage_data$Coverage)))

kp <- plotKaryotype(genome=genome, plot.type =4, cex=0.6)

kpPlotDensity(kp,data=cv, window.size=100000,r0=0,r1=0.2, col="#F8170C", border="#F8170C")

kx <-kpPlotDensity(kp,data=cv, window.size=100000,r0=0,r1=0.2, col="#F8170C", border="#F8170C")
kpAxis(kp, ymax=kx$latest.plot$computed.values$max.density/100, r0=0, r1=0.2, cex=0.4)
dev.off()

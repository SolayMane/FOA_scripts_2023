# FOA_Genomics

## Busco based phylogenomics
To generate busco based phylogenomics tree, we donwloaded 26 Fusarium genome from NCBI and mycocosm.jgi.doe.gov :
````bash
ls data/
Fusarium_graminearum_PH-1.fasta                         Fusarium_oxysporum_f.sp.cubense_race1.fasta
Fusarium_odoratissimum_Foc4_1.fasta                     Fusarium_oxysporum_f.sp._cubense_TR4.fasta
Fusarium_odoratissimum_NRRL54006.fasta                  Fusarium_oxysporum_f.sp.lycopersici_4287.fasta
Fusarium_oxysporum_f.sp._albedinis_9.fasta              Fusarium_oxysporum_f.sp.lycopersici_MN25.fasta
Fusarium_oxysporum_f.sp._albedinis_Foa133.fasta         Fusarium_oxysporum_f.sp.melonis_26406.fasta
Fusarium_oxysporum_f.sp._albedinis_Foa44.fasta          Fusarium_oxysporum_f.sp._narcissi_N139.fasta
Fusarium_oxysporum_f.sp._albedinis_Foa_Fmodqc.fasta     Fusarium_oxysporum_f.sp._pisi_HDV247.fasta
Fusarium_oxysporum_f.sp._albedinis_Foa_M12.fasta        Fusarium_oxysporum_f.sp.radicis-cucumerinum_Forc016.fasta
Fusarium_oxysporum_f.sp._cepae_FoC125.fasta             Fusarium_oxysporum_f.sp.radicis-lycopersici_26381.fasta
Fusarium_oxysporum_f.sp._cepae_FocA23.fasta             Fusarium_oxysporum_f.sp.raphani_54005.fasta
Fusarium_oxysporum_f.sp._cepae_FoCFus2.fasta            Fusarium_oxysporum_f.sp.vasinfectum_25433.fasta
Fusarium_oxysporum_f.sp.conglutinans_race2_54008.fasta  Fuscu1_AssemblyScaffolds.fasta
Fusarium_oxysporum_f.sp._cubense_160527.fasta           Fusso1_AssemblyScaffolds.fasta

# running the busco on the genome sequence
mkdir outBusco
for file in data/*.fasta
do
        output=$(basename ${file%%.fna*})


        busco -i $file -l sordariomycetes_odb10 -o $output -m genome --out_path outBusco --cpu 56
done

# create run folder and move all run_* folder to it
mkdir phyloRuns
find outBusco/ -type d -name "run_*" | while read path
do
        new_name=$(basename ${path%/*})
        cp -r $path phyloRuns/run_${new_name}
done

# Run the phylogenomics pipeline
python busco_phylo_fastree.py -t 56 -l sordariomycetes_odb10 --supermatrix -o phylOutput -d phyloRuns

# Root the tree suing the outgroup
python root.py phylOutput/SUPERMATRIX.tree  FusariumTree Fusarium_graminearum_PH-1.fasta

````
## Generation of fna files using buscomp
````bash
/usr/bin/python2.7 buscomp/code/buscomp.py runs="phylo/outBusco/*" \
fastadir="data/*.fasta"  \
metaeukfna=T \
buscompseq=F
````
## 

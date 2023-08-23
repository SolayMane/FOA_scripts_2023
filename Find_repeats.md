# Scritp to find repeats
## The workflow :
```bash


# Paths
RMoDR="/home1/software/RepeatModeler-2.0.4"

# Create a directory where you will store the repeat database and output files
mkdir repeats_db
cd repeats_db

# Run BuildDatabase
perl /home1/software/RepeatModeler-2.0.4/BuildDatabase -name foa44 Fusarium_oxysporum_f.sp._albedinis_Foa_44.scaffolds.fa 
cd ../

# Run RepeatModeler
nohup /home1/software/RepeatModeler-2.0.4/RepeatModeler -database repeats_db/foa44 --threads 56 -LTRStruct >& run.out &

# Run RepeatMasker
RepeatMasker -lib repeats_db/foa44-families.fa -dir repeats_masked -s -q -nolow -no_is -norna Fusarium_oxysporum_f.sp._albedinis_Foa_44.scaffolds.fa

# Run Parsing-RepeatMasker-Outputs script
perl Parsing-RepeatMasker-Outputs/parseRM.pl -i TE/repeat_masked/Fusarium_oxysporum_f.sp._albedinis_Foa_44.scaffolds.fa.out -p -v
````
use [plot_repeats_all.py](https://github.com/SolayMane/FOA_scripts/blob/main/plot_repeats_all.py) to generate the stats figure
![image](https://user-images.githubusercontent.com/22656460/225588029-98b99106-e80a-44dd-946b-1ae699b140cb.png)

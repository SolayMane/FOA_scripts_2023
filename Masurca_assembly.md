# The hybrid assembly was perfomed using the version MaSuRCA-3.4.0 with the fellowing parameters:

(JF_SIZE = 9000000000; CA_PARAMETERS = cgwErrorRate=0.15; SOAP_ASSEMBLY=0; FLYE_ASSEMBLY=0)
We use a confige file containg those parameters and the paths to the raw Illumina and ONT data (eg : sr_config_example.txt) then we run this command to obtain the backbone script of the assembly <code>assemble.sh</code>
````bash
# to obtaine the main assembly script based ont he config file
masurca sr_config_example.txt

# to run the assembly process
bash assemble.sh
````

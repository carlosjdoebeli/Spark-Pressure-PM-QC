# Spark-Pressure-PM-QC-

This code can be used with Spark instruments to qualify their pressure profiles. 

## Instructions of use

<b> Spark_PM&QC.py</b> should be used to get pressure profile data and qualify instruments. 
<b>Spark_Commercial.py</b> should be used for the same purpose, but only if the instrument is running on commercial code. For example, if the instrument is a customer instrument that is being serviced. 

To run these files, disassemble the outside case of the Spark instrument and connect your computer to the arduino microcontroller on the bottom of the Spark instrument with a Serial-to-USB converter. Run the relevant file, and input a file name according to a naming convention relevant to the test you are running. For example, <b>"065_Washer_1"</b>, where 065 is the instrument number.

Two data files will be created in the same folder as the script that is being run. One is a pressure data file, with the timestamp added to the test name. The other is a pressure graph, with no timestamp added. The code can easily be changed to include the timestamp for the graph file names if this is desired, by uncommenting line 141. The previous example would create files <b>"065_Washer_1 2019-01-18 14-19-13.647498.txt"</b> and <b>"065_Washer_1.png"</b>.

<b>Spark Graph Summarizer.py</b> can be used to easily summarize the graphs and overlays several graphs onto each other on the same graph for easy comparison. If several .txt files created by the Spark PM&QC code need to be overlaid on the same graph, place this script in the same folder as all of the desired text files. This script takes every text file in its root folder and creates a graph overlaying the data in one graphic. 

For the Spark Graph Summarizer script, the data must be separated by a ',' or ', ' and is unlikely to work as desired if any .txt files in the directory were not created by another script in this repository. 

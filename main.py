# NOTE: This file was maded for clean the results after execution of the scan, but we can easily loop all that program and make it sleep 5 seconds for example

import os # Import the "os" library for getting the files in the /tmp directory.
import re # Import the "re" library for using RegEx
# But, we can simply use "endswith .scan" if you don't know what is RegEx

files = os.listdir('/tmp') # We list all files in "/tmp" directory, it will be saved in a list, for example ["test.cpp", "Linux-SST.sh", "firefox-data.csv"]

for file in files: # We loop all content of "files" variable, the data will be saved at a string, for example "test.cpp" or "Linux-SST.sh"
    if re.findall(".*\.scan", file): # Filter "file" variable for seeing if it ends with ".scan", if yes it will continue or else it will simply go back to the "for" loop
        # ".*\.scan" is the regex expression, "file" is the name of file (for example "Linux-SST.sh" or "5c9D6c.scan")
        with open('/tmp/' + file, "w") as f: # It "opens" the file at the "f" variable, for editing it, in bash, we can simple use "echo 'Nothing found!' >> /tmp/FILE.scan"
            f.write("""
=================== Detections =================

==========================================================
Check explanation below!

Check A: Ilegal version/mod was found on minecraft folder
Check B: Ilegal modification in minecraft instance
Check C: unsecure check 


============== Minecraft instance time ============== 


============== Recycle Bin latest modification ==============



files
09:28
info
09:28
expunged
14:31

============== VPN Detection ============== 


============== NordVPN Detection ============== 

            """) # Replace the content of the file with a clean scan
            f.close() # Close the file for saving its contents

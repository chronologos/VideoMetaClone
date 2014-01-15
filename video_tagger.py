import os, shutil
import subprocess
import os.path
from datetime import datetime

sourceDir = os.getcwd() #Get current directory
mtsfiles = []
mp4files = []

for root, dirs, files in os.walk(sourceDir,True,None,True):
    for filename in files:
    	if filename[-4:] == '.MTS':
    		mtsfiles.append(filename)
    	elif filename[-4:] == '.mp4':
    		mp4files.append(filename)
#^^^ Get two lists of mts and mp4 files

for mts in mtsfiles:
	for mp4 in mp4files:
		if mts[:-4] == mp4[:-4]:
			creation_date =  datetime.fromtimestamp(os.stat(mts)[8])
			formatted_creation_date = creation_date.strftime('%Y%m%d%H%M.%S')
			command = "touch -t "+formatted_creation_date+" \""+mp4+"\""
			print command
			os.system(command)
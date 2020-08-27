#!/usr/bin/python3

import sys
#from os import path
import os.path
#import os
import easygui as eg 
avvio=0 

def creahtml():
	global avvio
	global directory
	if avvio==0 :
		#Apre file ino
		path = eg.fileopenbox(msg='Please locate INO file',
                    title='Link File', default='*.ino',
                    filetypes='*.ino')
		#print(path)
		directory=os.path.dirname(str(path))
		#print(directory)
		avvio=1
	else:
		default_dir=directory+"/*.ino"
		path = eg.fileopenbox(msg='Please locate INO file',
                    title='Link File', default=default_dir,
                    filetypes='*.ino')
		#print(path)
		directory=os.path.dirname(str(path))

	path_no_ext=path[:-4]
	path_ino=path_no_ext+"_f.ino"
	# Apre file htm
	fow = open(path_ino, "w")

	
	with open(path) as fin:
		for line in fin:
			if line.find('Serial.println(\"') > 0:
				#print(print_find)
				line=line.replace('Serial.println(\"','Serial.println(F(\"')
				line=line.replace(');','));')
				fow.write(line)
			
			elif line.find('Serial.print(\"') > 0:
				line=line.replace('Serial.print(\"','Serial.print(F(\"')
				line=line.replace(');','));')
				#print(line)
				fow.write(line)
			else:
				fow.write(line)

		
	# Close opend files
	fow.close()
	
	#eg.msgbox('File Convertito', 'Carica Link')


if __name__ == '__main__':
	ok=1
	while(ok==1):
		creahtml()
		msg = "Premi Continue per convertire un altro file..."
		title = "Carica File Ino"
		if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
			ok=1
		else:  # user chose Cancel
			sys.exit(0)

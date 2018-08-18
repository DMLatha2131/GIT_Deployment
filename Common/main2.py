#!/usr/bin/python
import fnmatch
import os
import re
import fileinput
import os.path
from os import path

def addPart(partfile, mainFile) :
	with open(partfile, "r") as part:		
		for line in part :
			
			line1 = line.replace('DemoPkg/src/', '')
			line1 = line1.split('\n')[0]
			
			if line1.endswith('.cls'):
				line1 = line1.split('.')[0] + '.*'
			elif line1.endswith('.cls-meta.xml'):
				line1 = line1.split('.')[0] + '.*'
			elif line1.endswith('.layout') :
				line1 = line1.split('.')[0].split('-')[0] + '-*.layout'
			elif line1.endswith('.component') :
				line1 = line1.split('.')[0]+ '.*'
			elif line1.endswith('.component-meta.xml') :
				line1 = line1.split('.')[0]+ '.*'
			elif line1.endswith('.page') :
				line1 = line1.split('.')[0]+ '.*'
			elif line1.endswith('.page-meta.xml'):
				line1 = line1.split('.')[0] + '.*'
			elif line1.endswith('.trigger') :
				line1 = line1.split('.')[0]+ '.*'
			elif line1.endswith('.trigger-meta.xml'):
				line1 = line1.split('.')[0] + '.*'
			elif line1.endswith('.email'):
				line1 = line1.split('.')[0] + '.*'
			elif line1.endswith('.email-meta.xml'):
				line1 = line1.split('.')[0] + '.*'
			mainFile.write("<fileset dir=\"DemoPkg\\src\" includes=\"" + line1 + "\"/>\n")
	
main  = open("build.xml", "a+")
main.truncate()

with open("part1.txt", "r") as diff:
	for line in diff :
		main.write(line)

addPart("diff.txt", main)

with open("part2.txt", "r") as diff:
	for line in diff :
		main.write(line)
import zipfile

unpack_dir = 'C:/Users/mdudekula/Desktop/Devops/Workspace/GIT_Deployment/Common/temp/'
import shutil
shutil.rmtree(unpack_dir)

print('Extracting ZIP.')
archive = zipfile.ZipFile('C:/Users/mdudekula/Desktop/Devops/Workspace/GIT_Deployment/deploy.zip', 'r')

# Extract to current directory
archive.extractall(unpack_dir)
print('ZIP Extracted.')
archive.close()

all_files=[]
pattern_found_in_files=[]
files_path='C:/Users/mdudekula/Desktop/Devops/Workspace/GIT_Deployment/Common/temp/classes/'

if os.path.exists(files_path) :
	dir = os.listdir(files_path)
	print(dir)
	for file in dir:
		if fnmatch.fnmatch(file,'*.cls'):
			all_files.append(file)
			#
	for file in all_files:
		abs_file=os.path.abspath(files_path+file)
		with open(abs_file,'r') as fp:
			file_data=fp.read()
			if re.search('@isTest',file_data, re.IGNORECASE):
				pattern_found_in_files.append(os.path.splitext(file)[0])
				print("Pattern found in the files:%s" % pattern_found_in_files)
	for listitem in pattern_found_in_files:
		main.write( '<runTest>' + listitem + '</runTest>\n')
	
main.write("</sf:deploy>\n")
main.write("</target>\n</project>")

main.close()

#os.system("ant DeployPartial")
#os.system("ant Deploy")

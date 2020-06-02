#!/usr/bin/env python

import sys
import os
import pathlib
import shutil


if len(sys.argv) < 3:
    print("Required arguments are missing")
    quit()

TEMPLATE_REPOSITORY = "terraform-provider-template"
PROJECT_DESCRIPTION = "@PROJECT_DESCRIPTION@"
PACKAGE_NAME = "template"

repository = sys.argv[1]
description = sys.argv[2]
package = repository.split('-')[2]

print(repository, description, package)

def replace_files(path, files):
	for filename in files:
		print(os.path.join(path, filename))
		replace_file(os.path.join(path, filename))


IGNORED_FILES = [".DS_Store", "LICENSE"]

def replace_file(fullpath):
	if IGNORED_FILES[0] in fullpath:
		return

	if IGNORED_FILES[1] in fullpath:
		return
		
	# read and replace text
	fin = open(fullpath, "rt")
	data = fin.read()
	data = data.replace(TEMPLATE_REPOSITORY, repository)
	data = data.replace(PROJECT_DESCRIPTION, description)
	data = data.replace(PACKAGE_NAME, package)
	data = data.replace(PACKAGE_NAME.capitalize(), package.capitalize())
	fin.close()
	
	# write replaced text
	fin = open(fullpath, "wt")
	fin.write(data)
	fin.close()

shutil.copytree(TEMPLATE_REPOSITORY, repository, ignore=shutil.ignore_patterns(".git"))

for path, subdirs, files in os.walk(repository):
	if ".git" not in path: 
		replace_files(path, files)	

os.rename(repository + "/template", repository + "/" + package)
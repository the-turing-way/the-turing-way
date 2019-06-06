#!/usr/bin/env python3
import os
import re
import sys


script_dir = os.path.dirname(__file__)
directory_to_check = os.path.join(script_dir,'../book/content/')


def remove_comments(text_string):
	p = re.sub('(?s)<!--(.*?)-->','', text_string)
	return p


def get_lines(text_string,sub_string):
	lines = [line for line in text_string.split('\n') if sub_string in line]
	return lines


bad_latin = ['i.e.','e.g.','e.t.c.',' etc', ' ie']
fails = {} # keys = filenames, values = (latin_type, line)
for root_dir, _, file_names in os.walk(directory_to_check):
	for file_name in file_names:
		file = open(os.path.join(root_dir,file_name),encoding="utf8", errors='ignore')
		text = file.read()
		text = remove_comments(text)
		for latin_type in bad_latin:
			if latin_type in text.lower():
				for line in  get_lines(text.lower(),latin_type):
					try:
						fails[os.path.abspath(file.name)].append((latin_type, line))
					except:
						fails[os.path.abspath(file.name)] = [(latin_type, line)]


if len(fails.keys())!=0:
	error_message = 'Bad latin found in the following files:\n\n'
	for file_loc in fails.keys():
		error_message += file_loc + '\n'
		for instance_of_fail in fails[file_loc]:
			latin_type, line = instance_of_fail
			error_message += latin_type + '\t found in line \t"' + line + '"\n'
		error_message += '\n'
	raise Exception(error_message) 


#!/usr/bin/env python3

import os
import re

 # TODO: (?) Update to check whole book
directory_to_check = '../book/content/reviewing/'

def remove_comments(text_string):
	p = re.sub('(?s)<!--(.*?)-->','', text_string)
	return p

for file_path in os.listdir(directory_to_check):
	file = open(os.path.join(directory_to_check,file_path), 'r')
	text = file.read()
	text = remove_comments(text)
	assert ('lorem ipsum' not in text.lower())
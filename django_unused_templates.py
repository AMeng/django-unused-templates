"""
Django Unused Templates
by Alexander Meng

Generates a list of unused templates in your current directory and subdirectories
by searching all .html and .py files for the names of your templates.

IF YOU OVERRIDE DJANGO TEMPLATES, THEY MAY APPEAR IN THE LIST AS UNUSED.

"""

import fileinput, string, os

def get_html_files():
	return [f[2:-1] for f in os.popen("find . -name '*.html' | sort").readlines()]

def get_py_files():
	return [f[2:-1] for f in os.popen("find . -name '*.py' | sort").readlines()]

def get_templates():
	#Templates will only be returned if they are located in a /templates/ directory
	template_list = []
	for html_file in get_html_files():
		if html_file.find("templates/") != 0:
			try:
				template_list.append(html_file.rsplit("templates/")[1])
			except IndexError: #The html file is not in a template directory... don't count it as a template
				template_list.append("html")
	
	return template_list

def get_unused_templates():

	templates = get_templates()
	html_files = get_html_files()
	py_files = get_py_files()
	files = py_files + html_files #List of all files
	tl_count = [0 for t in templates]

	for count, template in enumerate(templates):
		for line in fileinput.input(files): #Loops through every line of every file
			if line.find(template) > 0:
				tl_count[count] = 1

		if tl_count[count] == 0:
			print(html_files[count])

if __name__ == "__main__":
	get_unused_templates()


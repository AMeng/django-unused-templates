"""
Django Unused Templates
by Alexander Meng

Generates a list of unused templates in your current directory and subdirectories
by searching all .html and .py files for the names of your templates.

IF YOU OVERRIDE DJANGO TEMPLATES, THEY MAY APPEAR IN THE LIST AS UNUSED.

"""

import argparse
import fileinput
import os


def get_files(extension, skip):
    cmd = f"find . -name '*.{extension}'"
    if skip:
        for dir in skip:
            cmd += f" -not -path './{dir}/*'"
    cmd += " | sort"
    return [f[2:-1] for f in os.popen(cmd).readlines()]


def get_templates(html_files):
    # Templates will only be returned if they are located in a
    # /templates/ directory
    templates = {}
    for html_file in html_files:
        try:
            template = html_file.rsplit("templates/")[1]
            templates[template] = {'file': html_file, 'count': 0}
        except IndexError:
            # The html file is not in a template directory...
            # don't count it as a template
            pass

    return templates


def get_unused_templates(skip, fast, filename):
    html_files = get_files('html', skip)
    py_files = get_files('py', skip)
    files = py_files + html_files  # List of all files
    templates = get_templates(html_files)

    files_content = None
    output = []

    # If -f or --fast parameter is given
    # load entire data to memory to speed up execution.
    # Otherwise reread files on every pass
    if fast:
        files_content = list(fileinput.input(files))

    for template in templates:
        if fast:
            lines = files_content
        else:
            lines = fileinput.input(files, openhook=fileinput.hook_encoded("utf-8"))

        for line in lines:
            if line.find(template) > 0:
                templates[template]['count'] += 1

        if templates[template]['count'] == 0:
            if not filename:
                print(templates[template]['file'])
            else:
                output.append(templates[template]['file'])

    if filename:
        with open(filename, 'w') as f:
            f.writelines('\n'.join(output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--skip', default=[], nargs='*')
    parser.add_argument('-f', '--fast', action='store_true')
    parser.add_argument('-o', '--output', default=None)
    options = parser.parse_args()
    get_unused_templates(options.skip, options.fast, options.output)

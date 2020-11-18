## Django Unused Templates

checks your Django project for unused templates.

## Usage

To use, navigate to your desired directory (could be your top level) and run the script through python:

```sh
python django-unused-templates.py
```

It gathers the file names of all .html files that sit in a /templates/ directory, and subdirectories. It 
then checks all .py files and .html files for an instance of this name. This covers all possible uses of 
the template file. If the template file is not referenced in any of the other files in your project, it 
is considered .unused.. The script will display a list of all unused templates. 

## Options

Script has a number of options:
- `-s` or `--skip`: skip desired directories and subdirecories entirely
  ```sh
  # do not search in venv directory
  python django-unused-templates.py --skip venv
  # do not search in app1 and app2 directories
  python django-unused-templates.py -s app1 app2
  ```
- `-f` or `--fast`: work faster at the expense of higher memory usage
  ```sh
  python django-unused-templates.py -f
  ```
- `-o` or `--output`: print results into file, instead of stdout
  ```sh
  # will output result to unused.txt
  python django-unused-templates.py -o unused.txt
  ```

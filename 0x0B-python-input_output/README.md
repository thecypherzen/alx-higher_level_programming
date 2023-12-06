# Overview #

This directory contains everything about the **Python - Input/Output** project, which are required for fulfilling the requirements of the project. Non-required files are in respective directors, named accordingly.

### Project Timeline Details ###
- **Released:** Tue Dec. 5, 2023 - 6am.
- **1st Deadline:** Wed Dec. 6, 2023 - 6am.
- **Duration:** 24 hrs (1 day).
- **Month** 5, **Week** 1, **Day** 2.

## Author ##
- [William Inyam](https://github.com/thecypherzen/)

### Technologies ##
- All C files(if any) written to be C-89 compatible and compiled with gcc 9.4.0.
- All Python files written and tested with Python 3.8.10.
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- Code tested on Ubuntu 20.04 LTS.

## File Tree ##
	ROOT
	| - README.md
	| - All task files and modules
	| - tests
		| - all test files


## Files ##
Files on the project are task based and are as follows:
| SN | File | Description |
|----|------|-------------|
| 1. | README.md | Folder Readme file |
| 2. |[0-read_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/0-read_file.py)  | A function that reads a text file (UTF8) and prints it to stdout:<ul><li>the <em>with</em> statement must be used.</li><li>module imports not allowed.</li><li>module imports not allowed.</li><li>no need to manage file permission or file doesn't exist exceptions.</li></ul>. |
| 3. | [1-write_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/1-write_file.py) | A function that writes a string to a text file in UTF-8 encoding and returns the number of characters written:<ul><li>should create file if it doesn't exist and overwrite it if it does.</li><li>the <em>with</em? statement must be used.</li><li>module imports not allowed.</li><li>don’t need to manage file permission exceptions.</li></ul> |
| 4. | [2-append_write.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/2-append_write.py) | A function that appends a string at the end of a text file in utf-8 encoding and returns the number of characters added:<ul><li>the <em>with</em? statement must be used.</li><li>module imports not allowed.</li><li>don’t need to manage file permission exceptions.</li></ul> |
| 5. | [3-to_json_string.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/3-to_json_string.py) | A function that returns the JSON representation of an object (string).<ul><li>don’t need to manage exceptions if the object can’t be serialized.</li></ul> |
| 6. | [4-from_json_string.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/4-from_json_string.py) | A function that returns an object (Python data structure) represented by a JSON string:<ul><li>don’t need to manage exceptions if the JSON string doesn’t represent an object.</li></ul> |
| 7. | [5-save_to_json_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py) | A function that writes an Object to a text file, using a JSON representation:<ul><li>the <em>with</em? statement must be used.</li><li>don’t need to manage exceptions if the object can’t be serialized.</li><li>don’t need to manage file permission exceptions.</li></ul> |
| 8. | [6-load_from_json_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py) | A function that creates an Object from a *“JSON file”*:<ul><li>the <em>with</em? statement must be used.</li><li>don’t need to manage exceptions if the JSON string doesn’t represent an object.</li><li>don’t need to manage file permission exceptions.</li></ul> |
| 9. | [7-add_item.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/7-add_item.py) | A script that adds all arguments to a Python list, and then save them to a file:</li><li>must use the function **save_to_json_file** from [5-save_to_json_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py)</li><li>must use the function **load_from_json_file** from [6-load_from_json_file.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py).</li><li>The list must be saved as a JSON representation in a file named **add_item.json**</li><li><li>If the file doesn’t exist, it should be created</li>don’t need to manage file permission or exceptions.</li></ul> |
| 10. | [8-class_to_json.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py) | A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:<ul><li>Prototype: def class_to_json(obj):</li><li>obj is an instance of a Class.</li><li>All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean.</li><li>no module imports allowed.</li></ul> |
| 11. | [9-student.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/9-student.py) | A a class Student that defines a student by:<ul><li>Public instance attributes: *first_name*, *last_name*, and *age*.</li><li>oInstantiation with first_name, last_name and age.</li><li>Public method def to_json(self): that retrieves a dictionary representation of a Student instance.</li><li>no module imports allowed.</li></ul> |
| 12. | [10-student.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py) | An extension of **(11)** above:<ul><li>modifies *to_json(self)* to *to_json(self, attrs=None)* such that: .<ul><li>If **attrs** is a list of strings, only attribute names contained in this list must be retrieved</li><li>if not, all attributes must be retrieved</li></ul></li><li>no module imports allowed.</li></ul> |
| 13. | [11-student.py](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x0B-python-input_output/11-student.py) | extends **(12)** above: adds method *reload_from_json* to class: <ul><li>a method that replaces all attributes of the Student instance.</li><ul><li>assumes json will always be a dictionary</li><li>a dictionary key will be the public attribute name</li><li>a dictionary value will be the value of the public attribute</li></ul><li>no module imports allowed.</li></ul> *The purpose of **tasks 11-13** is to build a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)*|

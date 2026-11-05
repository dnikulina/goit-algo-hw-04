# Python File Handling & CLI Practice

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat-square)
![Pathlib](https://img.shields.io/badge/pathlib-File%20System-lightgrey?style=flat-square)
![Colorama](https://img.shields.io/badge/Colorama-Terminal%20Output-yellow?style=flat-square)

## Overview

This repository contains four Python exercises focused on file processing, structured data extraction, recursive directory traversal, and building a simple command-line contact assistant.

## Tech Stack

- Python
- File I/O
- `pathlib`
- `sys`
- Colorama
- Command Line Interface

## Tasks

### 1. Salary Statistics

[first_task.py](./first_task.py)

Reads salary data from a text file and calculates:

- total salary;
- average salary.

Includes basic file error handling.

### 2. Cat Information Parser

[second_task.py](./second_task.py)

Reads structured cat records from a text file and converts them into a list of dictionaries containing:

- ID;
- name;
- age.

### 3. Directory Structure Viewer

[third_task.py](./third_task.py)

Displays a recursive directory tree from a path passed through the command line.

The script:

- validates whether the path exists;
- checks that the path is a directory;
- recursively traverses nested folders;
- uses colors to distinguish files and directories.

### 4. Contact Assistant

[forth_task.py](./forth_task.py)

Implements a basic CLI contact manager with commands to:

- add contacts;
- update phone numbers;
- search for phone numbers;
- display all contacts;
- exit the application.

## Learning Outcomes

This homework helped me practice:

- reading and parsing text files;
- working with dictionaries and lists;
- exception handling;
- filesystem navigation;
- recursion;
- command-line arguments;
- building a simple interactive CLI application.

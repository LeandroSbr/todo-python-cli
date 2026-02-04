# todo-python-cli

A simple command-line interface (CLI) to-do list application in Python.
This application allow you to add, remove, filter and sort tasks easily from your terminal, and save them is a JSON file.

## Description

- **main.py**: Main file with CLI inteface and logic.
- **to_do_class.py**: Class implementatio, whith his methods and logic.

JSON file not in the repo, but the program will generate it automatically

## Features

1. **Add**: Add a new task to the list, entering the name, the deadline, and the priority.
2. **Mark activity**: Mark added tasks ad done or as to-do.
3. **Filter activity**: Filter activities by priority, and show only done activities or to-do activities.
4. **Remove**: Remove activity from you list
5. **View**: View all the task from your list.
6. **Exit**: Exit the application and save all in a JSON file.

## Installation

Clone the repo from GitHub:

```bash
git clone git@github.com:LeandroSbr/todo-python-cli.git
cd to-do-list
```

## Usage

Run the application:

```bash
python main.py
```

Follow the on-screen prompt to interact with the program.

## Example

```bash
=== TO Do LIST ===

Choose an option: 
1) Add activity
2) Mark activity as done
...
9) Quit
- 1
Name of the activity:
Deadline (DD/MM/YY):
Priority (High, Medium, Low):
Activity registered
```

---

Enjoy using the to-do-list!

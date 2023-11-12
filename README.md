0x00. AirBnB clone - The console

Project description
This project is built to clone AirBnB.

Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

The console is a command interpreter to manage objects abstraction between objects and how they are stored


Classes are handled by storage engine and filestorage Class.

Here are the listed features of the console

Creat new object
Retrieve object from a file
perform operations on objects
destroy and object



All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.


All tests are defined in the test folder.

python3 -c 'print(__import__("my_module").__doc__)'

python3 -c 'print(__import__("my_module").MyClass.__doc__)'

python3 -c 'print(__import__("my_module").my_function.__doc__)'


unittest module is used for the Python unit tests.


To start the console in intereactive mode, use:
$ ./console.py
(hbnb)

Commands allowed in the console

All, create, destroy, count, show, update

For help: 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

To quit:
(hbnb) quit
$

Authors
Adeola Damilola
Oyeyemi Adeniji


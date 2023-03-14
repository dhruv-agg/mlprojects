"""
When you run python src.py, you are executing the Python interpreter and telling it to execute the src.py script. This assumes that src.py is located in the current working directory.

When you run python -m src.py, you are telling the Python interpreter to treat src.py as a module and run it using the -m flag. This assumes that src.py is located in a module directory that is on the Python path.

The main difference between the two approaches is that running a script directly (python src.py) runs the code in the script as the main program, while running a module (python -m src.py) executes the code in the module as if it were imported as a module, and the code in the __name__ == '__main__' block is also executed.

Another difference is that when you use -m flag, the sys.path is modified to include the current directory of the script as the first element. This means that if your script depends on other modules in the same directory, they will be found when you run python -m src.py, but not necessarily when you run python src.py.

In general, if you want to execute a script directly, use python src.py. If you want to import a module and run it as if it were the main program, use python -m src.py.
"""

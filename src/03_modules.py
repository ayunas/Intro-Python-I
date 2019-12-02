"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for x in sys.argv:
    print('elements in sys.argv array:', x)


# Print out the OS platform you're using:
# YOUR CODE HERE
# print(sys.platform)

def get_platform():
    # print("sys.platform: ", sys.platform)
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }

    # for plat in platforms:
    #     print(plat)

    if sys.platform not in platforms:
        print(sys.platform)
    
    print(platforms[sys.platform])

get_platform()

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python Version: ", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Process ID: ", os.getpid())


# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Working Directory", os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE
print('User login name: ', os.getlogin())



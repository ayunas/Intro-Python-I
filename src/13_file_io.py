"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

foo = open("foo.txt", 'r')
print(foo.read())
foo.close()

if foo.closed:
    print('Foo file has been closed')
else:
    print('Foo file is still open')







# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

bar = open("./bar.txt", "w")
bar.write("this is the bar text")
bar.close()

bar = open("bar.txt")
print(bar.read())
bar.close()

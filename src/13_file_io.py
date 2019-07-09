"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open("foo.txt") as f:
    read_file = f.read()
    print(read_file)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
with open("bar.txt", "w+") as f:
    write_file = f.write("This is a test.\n I'm writing jibberish.\n Let's see how it turns out\n")
    read_file = f.read()
    print(read_file)

# YOUR CODE HERE
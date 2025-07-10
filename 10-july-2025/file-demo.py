# File Objects
from os import close

# Context Manager
with open('test.txt', 'r') as f: # outside of this scope the file gets closed, no need to explicitly close it

    """to read files having large amount of data, this doesn't read the whole file as a whole but reads it one-by-one"""
    for line in f:
        print(line, end='')

    """Ok if we have a file with small amount of content"""
    f_contents = f.readline( )
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

    """ito have more control over the content being read"""
    f_contents = f.read(50)
    print(f_contents)
    f_contents = f.read(50)
    print(f_contents)

"""Not recommended"""
# f = open('test.txt', 'r')
# print(f.name)
# f.close()
# File Objects
from os import close

# Context Manager
with open('test.txt', 'r') as f: # outside of this scope the file gets closed, no need to explicitly close it

    """to read files having large amount of data, this doesn't read the file as a whole but reads it one-by-one"""
    # for line in f:
    #     print(line, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)

    """After the first 10 characters are displayed, seek(0) tells that the next 10 characters should be printed starting from character 0"""
    f.seek(0)

    # Will print the next 10 chars from the starting of the file
    f_contents = f.read(size_to_read)
    print(f_contents)

    """ tells at which position we are at in the file, like konsi line read kar rhe"""
    print(f.tell())

    """Ok if we have a file with small amount of content"""
    # f_contents = f.readline( )
    # print(f_contents, end='')
    #
    # f_contents = f.readline()
    # print(f_contents, end='')

    """to have more control over the content being read"""
    # f_contents = f.read(50)
    # print(f_contents)
    # f_contents = f.read(50)
    # print(f_contents)

"""Not recommended"""
# f = open('test.txt', 'r')
# print(f.name)
# f.close()
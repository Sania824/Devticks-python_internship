import os

print(os.getcwd())
os.chdir('/home/sania/Desktop')
print(os.getcwd())

os.mkdir('demo2')
os.makedirs('demo3/sub-demo3')
os.rmdir('demo2')
os.removedirs('demo3/sub-demo3')

os.rename('test.txt', 'demo.txt')
print(os.stat('os_module.py').st_size)
for dirpath, dirname, filenames in os.walk('/home/sania/Desktop'):
    print("Current Directory: ", dirpath)
    print("Directories: ",dirname)
    print("Filenames: ", filenames)
    print()

print(os.environ.get('HOME'))
"""TO make a new file and figure out its path, use os.path.join instead od String slicing or guessing where to put the slashes"""
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))
print(os.path.isfile('/home/sania/Desktop/Devticks-python_internship/10-july-2025/builtin_funcs_practice.py'))
print(os.path.isdir('/home/sania/Desktop/Devticks-python_internship'))

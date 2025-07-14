try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception # manual exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executed Successfully!')
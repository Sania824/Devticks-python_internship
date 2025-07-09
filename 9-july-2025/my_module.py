print("Imported module successfully")

test = "Test String"
def find_index(to_search, target):
    """Find the index of a value in the sequence"""
    for i, value in enumerate(to_search, start=0):
        if value == target:
            return 1
    return -1
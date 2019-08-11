import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents"""
    total = os.path.getsize(path)                      # account for direct usage
    if os.path.isdir(path):                            # if this is a diectory
        for filename in os.listdir(path):              # then for each child
            childpath = os.path.join(path, filename)   # compose full path to child
            total += disk_usage(childpath)             # add child' usage to total
    print('{0:<5}'.format(total), path)                #describle output(optional)
    return total                                       # return grand total

print(disk_usage("/mnt/e/sub/ProgrammingTest/algorithms/"))
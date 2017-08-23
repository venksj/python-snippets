
def sort_fruits(oldFile, newFile):
    try:
        unsortedFile = open(oldFile, 'r')
    except:
        print "File (%s) not found!!" %(oldFile)
        return 0

    l = unsortedFile.readlines()
    unsortedFile.close()
    l.sort()

    sortedFile = open(newFile, 'w')
    sortedFile.truncate(0)
    sortedFile.writelines(l)
    sortedFile.close()

    return 0

if __name__ == '__main__':
    sort_fruits('unsorted.txt', 'sorted.txt')



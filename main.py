
import os,stat

def is_hidden(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def lock():
    pass


def unlock():
    pass


def list_dir():
    flist = os.listdir(".")
    print(flist)
    i=0
    for item in flist:
        i+=1
        print(f'{i} {item}')
    
    n = int(input(">> "))
    test = os.system(f'attrib {flist[n-1]}')

def main():
    print(is_hidden('test.txt'))

if __name__ == "__main__":
    main()





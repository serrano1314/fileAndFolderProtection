
import os,stat

def is_locked(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_SYSTEM)

def set_password():
    while(1):
        lockPassword = input('Please Enter a Password:')
        verifyPassword = input('Type Again Password:')

        if lockPassword == verifyPassword:
            return lockPassword
        else:
            print('Password doesn\'t match')
            continue

def lock(filename):
    os.system('@echo off')
    os.system(f'attrib +s +h {filename}')
    create_unlocker(filename)

def create_unlocker(filename):
    fname_wo_ext = filename.split('.')[0] + '.bat'
    with open(fname_wo_ext,'w') as f:
        f.write('@echo off\n')
        f.write(f'attrib -s -h "{filename}"')


def list_dir():
    flist = os.listdir(".")
    i=0
    for item in flist:
        i+=1
        print(f'{i} {item}')
    # print('>>', flist[3].split('.')[0] )
    # n = int(input(">> "))
    # test = os.system(f'attrib {flist[n-1]}')

def main():
    print('SELECT ACTION:')
    print('[1] Lock')
    print('[2] Unlock')
    print('[X] Exit')
    print(set_password())


if __name__ == "__main__":
    main()





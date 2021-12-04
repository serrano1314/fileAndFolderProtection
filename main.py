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


def lock():
    list_dir()
    n = int(input('> '))
    if n==0:
        return

    filename = FLIST[n-1]
    pw = set_password()
    os.system('@echo off')
    os.system(f'attrib +s +h "{filename}"')
    print('Locking Successful')
    create_unlocker(filename,pw)


def create_unlocker(filename,pw):
    batchFile = filename.split('.')[0] + '.bat'
    with open(batchFile,'w') as f:
        f.write('@echo off\n')
        f.write('setlocal\n')
        f.write('set /p inputPw=Type Password:\n')
        f.write(f'set pw={pw}\n')
        f.write(f'if "%pw%" equ "%inputPw%" ( \n')
        f.write(f'attrib -s -h "{filename}"\n')
        f.write(f'del "{batchFile}"\n')
        if '.' in filename:
            f.write(f'"{filename}"\n')
        else:
            f.write(f'explorer.exe "{filename}"\n')
        f.write('pause\n')
        f.write(') else ( echo Wrong Password. Program will Exit. ) \n')
        f.write('endlocal \n')
        f.write('pause')


def list_dir():
    print('Select a file/folder:')
    i=1
    for item in FLIST:
        print(f'\033[0m', end='')
        if is_locked(item):
            print(f'[{i}]', end='')
            print(f'\033[91m {item} [LOCKED]')
        else:
            print(f'[{i}]', end='')
            print(f'\033[92m {item}')

        i+=1
    print(f'\033[0m')
    # print('>>', flist[3].split('.')[0] )
    # n = int(input(">> "))
    # test = os.system(f'attrib {flist[n-1]}')

def main():
    global FLIST
    FLIST = os.listdir(".")
    print('SELECT ACTION:')
    print('[1] Lock')
    print('[2] Unlock')
    print('[X] Exit')
    choose = input('> ')
    if(choose == '1'):
        lock()
    elif(choose == '2'):
        pass
    else:
        return


if __name__ == "__main__":
    main()





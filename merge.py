import glob
import os
import sys

EXTENTION = '.utfonly.wx'
TIMESTAMP_LENGHT = 12
EXTRA_LENGTH = 1

OUTPUT_EXTENTION = '.txt'

def remove_the_file(file):
    os.remove(file)

def get_data_from_the_file(file):
    data = ''
    with open(file,'r') as f:
        data = f.read()
    return data

def get_timestamp(filename):
    total_length = EXTRA_LENGTH+len(EXTENTION)+TIMESTAMP_LENGHT
    merge_file = filename[:-total_length]
    time_stamp = filename[-total_length:].replace('_','').replace(EXTENTION,'')
    if not time_stamp.isnumeric() or len(time_stamp)!=TIMESTAMP_LENGHT:
        time_stamp = ''
        merge_file = filename.replace(EXTENTION,'')
    return merge_file,time_stamp

def get_dir_filename(path): 
    i = len(path)-1
    while i>-1:
        if path[i] == '/':
            break
        i-=1
    return path[:i+1],path[i+1:]

def main():
    path = ''
    try:
        path = sys.argv[1]
        path = path if path[-1]=='/' else path+'/'
    except:
        print('working on current directory')
    for file in glob.glob('%s**/*%s'%(path,EXTENTION),recursive=True):
        data = get_data_from_the_file(file)
        dir,filename = get_dir_filename(file)
        merge_file,stamp = get_timestamp(filename)
        with open(dir+merge_file+OUTPUT_EXTENTION,'a') as f:
            f.write('\n#TIMESTAMP:%s\n'%stamp)
            f.write(data)
        remove_the_file(file)

if __name__ == "__main__":
    main()
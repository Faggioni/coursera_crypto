import sys
def split_file(name,size):
    f = open(name,'rb')
    video = f.read()
    f.close()
    data = []
    for i in range(0,len(video),size):
        if ((i + size) < len(video)):
            data.append(video[i:i+size])
        else:
            data.append(video[i:])
    return data

def splitting(name,size):
    f = open(name,'rb')
    video = f.read()
    f.close()
    data = []
    string =''
    for byte in video:
        string += byte
        if (sys.getsizeof(string) == 1024):
            data.append(string)
            string=''
    return data



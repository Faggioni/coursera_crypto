def split_file(name,size):
    f = open(name,'rb')
    video = f.read()
    f.close()
    data = []
    for i in range(0,len(video),size):
        if ((i + size - 1) < len(video)):
            data.append(video[i:i+size-1])
        else:
            data.append(video[i:])
    return data






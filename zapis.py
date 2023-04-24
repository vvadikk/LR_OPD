def vfile(a, b):
    f = open('top250.txt', 'w')
    for i in range(250):
        f.write(str(i+1)+' '+a[i]+' '+b[i]+'\n')
    f.close()
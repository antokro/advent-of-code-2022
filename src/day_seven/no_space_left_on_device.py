currentPath=[]
folders={}
def pathToString(pathList):
    print(pathList)
    out=''
    if len(pathList)==1:
        return '/'
    for e in pathList:
        if out=='':
            out=e
        elif out[-1] =='/':
            out+=e
        else:
            out+='/'+e
    return out

def no_space_left_on_device(filesystem: list):
    for l in filesystem:
        if "$ cd .." in l:
            currentFolder=currentPath.pop()
            strPath=pathToString(currentPath)
        elif "$ cd" in l:
            currentFolder=l.split()[-1]
            currentPath.append(currentFolder)
            strPath=pathToString(currentPath)
            if strPath not in folders.keys():
                folders[strPath]=0
        elif l.split()[0].isdigit():
            fsize,fname=l.split()
            for i in range(len(currentPath)-1,0,-1):
                parentPath=pathToString(currentPath[:i])
                folders[parentPath]+=int(fsize)
            folders[strPath]+=int(fsize)
    # part 1
    totalSum=0
    print(folders)
    for f in folders.keys():
        if folders[f]<=100000:
            totalSum+=folders[f]

    #part 2
    freeMem=70000000-folders['/']
    minSize=freeMem
    for f in folders.keys():
        if folders[f]+freeMem>=30000000:
            if folders[f]<minSize:
                minSize=folders[f]
    
    return (totalSum, minSize)



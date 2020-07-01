# def towerofhanoi(numberofdisk, startpeg=1, endpeg=3):
#     if numberofdisk:
#         towerofhanoi(numberofdisk-1, startpeg, 6-startpeg-endpeg)
#         print("move disk %d from peg %d to peg %d" %(numberofdisk, startpeg, endpeg))
#         towerofhanoi(numberofdisk-1, 6-startpeg-endpeg, endpeg)
# towerofhanoi(numberofdisk=3)


def Towerofhanoi(n, source, destination, auxiliary):
    if (n==1):
        print("move disk 1 from source ", source, "to destination ", destination)
        return
    Towerofhanoi(n-1, source, auxiliary, destination)
    print("move disk", n, "from source ", source,"to destination ", destination)
    Towerofhanoi(n-1, auxiliary, destination, source)

n=3
Towerofhanoi(n,'A',"B","C")
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

open('database.txt','w').close()
def data():
    num=range(0,10)
    ver=range(1,10)
    datafile=open('database.txt','a')
    for n in num:
        for v in ver:
            path='images/numbers/'+str(n)+'.'+str(v)+'.png'

            ei=Image.open(path)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())

            linewrite=str(n)+'::'+eiar1+'\n'
            datafile.write(linewrite)


def threshold(arr):
    balance=[]
    newarr=arr
    for row in arr:
        for pix in row:
            avg=int(sum(pix[0:3])/3)
            balance.append(avg)
    print(balance)
    bal=int(sum(balance)/len(balance))
    print(bal)
    for r in newarr:
        for pixx in r:
            if int(sum(pixx[0:3])/3)>=bal:
                pixx[0]=255
                pixx[1]=255
                pixx[2]=255
                pixx[3]=255
            else :
                pixx[0]=0
                pixx[1]=0
                pixx[2]=0
                pixx[3]=255
    return newarr

data()
def findnum(path):
    match=[]
    load=open('database.txt','r').read()

    load=load.split('\n')
    i=Image.open(path)
    iar=np.array(i)
    iar=threshold(iar)
    iarl=iar.tolist()
    iquestion=str(iarl)

    for ex in load:
       if len(ex)>3:
            splitex=ex.split('::')
            currentnum=splitex[0]
            currentarray=splitex[1]
            eachpixex=currentarray.split('],')
            eachpixinq=iquestion.split('],')

            x=0

            while x < len(eachpixex):
                if eachpixex[x]==eachpixinq[x]:
                    match.append(int(currentnum))
                x+=1



    print(match)
    x=Counter(match)
    #print (x)
    graphx=[]
    graphy=[]
    for i in x:
        print(i)
        graphx.append(i)
        print(x[i])
        graphy.append(x[i])

    fig=plt.figure()
    ax1 =  plt.subplot2grid((4,4),  (0,0),  rowspan=1, colspan=4)
    ax2 =  plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(graphx,graphy,align='center')
    plt.ylim(400)

    xloc=plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()


findnum('images/test.png')


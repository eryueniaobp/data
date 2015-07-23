__author__ = 'baipeng'
import  re
from operator import itemgetter, attrgetter
import numpy as np
import matplotlib.pyplot as plt
import pylab,datetime

def trend_rate(values):
    diff = []
    for i in range(1,len(values)):
        diff.append(values[i] - values[i-1])

    cnt = 0.0
    for i in range(1,len(diff)):

        prev = diff[i-1]
        cur = diff[i]
        if cur*prev >= 0 :
            cnt +=1

    return cnt/(len(diff)+1) #avoid divide zero





with open('data','r') as f:
    catemap = {

    }
    for line in f:
        line = line.strip()
        date,cate,ecpm = re.split(",|\t",line)

        if cate not in catemap:
            catemap[cate] = []
        catemap[cate].append( (date ,float(ecpm) ) )

    cate2trend = {

    }
    fig = plt.figure()
    for cate in catemap:

        if cate not in ['GAME','MUSIC']:
            continue

        values = catemap[cate]
        values = sorted(values,key=itemgetter(0) )
        x = [ datetime.datetime.strptime(i[0],"%Y%m%d") for i in values]
        y = [ i[1] for i in values]
        cate2trend[cate] = trend_rate(y)

        fcate = plt.plot_date(pylab.date2num(x),y ,linestyle='-',label='{cate} {rate}'.format(
            cate=cate,
            rate = int(cate2trend[cate]*100)/100.
        ))

        # plt.legend(cate)
    # handles ,labels = plt.get_legend_handles_labels()
    # plt.legend(handles,labels)
    plt.legend()
    plt.grid()
    plt.savefig('trend')
    plt.show()
    for cate in cate2trend:
        print '{cate}\t{rate}'.format(cate=cate,rate=cate2trend[cate])
    # print cate2trend



pass



import datetime as dt
import random
with open('data','w') as f:
    catelist = ["GAME","MUSIC","PHOTO"]
    for i in xrange(100):
        today = dt.datetime.today()
        delta = dt.timedelta(days=-i)

        day  =today + delta

        day = day.strftime("%Y%m%d")

        cate  = random.choice(catelist)


        ecpm  = random.randint(10,50)

        print '{day}\t{cate}\t{ecpm}'.format(
            day = day,
            cate = cate,
            ecpm = ecpm
        )




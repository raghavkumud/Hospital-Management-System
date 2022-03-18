import getpass
import datetime as dt
import copy
import mysql.connector
from mysql.connector import Error


def camp_info(cursor):
    ls = []
    cursor.execute('select event_name from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls


def event_timings(cursor):
    ls = []
    cursor.execute('select event_stime,event_etime from all_events')
    for i in cursor:
        ll = []
        ll.append(i[0])
        ll.append(i[1])
        ls.append(ll)
    return ls


def event_place(cursor):
    ls = []
    cursor.execute('select event_place from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls


def event_date(cursor):
    ls = []
    cursor.execute('select event_date from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls


def convert_deltatime(delta):
    s = int(delta.total_seconds())
    hh = s//3600
    s %= 3600
    mm = s//60
    s %= 60
    ss = s

    d_time = dt.time(hh, mm, ss)
    d_s = d_time.strftime('%I:%M %p')
    return d_s


def give_info(cursor):
    en = camp_info(cursor)
    et = event_timings(cursor)
    ep = event_place(cursor)
    ed = event_date(cursor)
    index = -1
    dd = dt.date(2022, 2, 10)
    #dd = dt.date.today()
    print(dd)
    for i in range(len(ed)):
        if dd == ed[i]:
            # print(ed[i])
            index = i
            break

    if index != -1:
        print(en[index], et[index], ep[index], ed[index])
        stime = convert_deltatime(et[index][0])
        etime = convert_deltatime(et[index][1])
        print(stime, etime)
        date_format = ed[index].strftime('%B %d, %Y')
        print(date_format)
        index = -1
        inf = f"Free {en[index]} Check Up Camp is being organised on {date_format} from {stime} to {etime} at {ep[index]} ."
        return inf

    return ""


def all_events(cursor):
    en = camp_info(cursor)
    et = event_timings(cursor)
    ep = event_place(cursor)
    ed = event_date(cursor)

    n = len(en)
    lis = []
    cur_date = dt.date.today()
    for i in range(n):
        print(ed[i], ed[i] > cur_date)
        if ed[i] >= cur_date:
            stime = convert_deltatime(et[i][0])
            etime = convert_deltatime(et[i][1])

            date_format = ed[i].strftime('%B %d, %Y')
            ss = f"Free {en[i]} Check Up Camp is being organised on {date_format} from {stime} to {etime} at {ep[i]} ."
            lis.append(ss)

    return lis


def check_info(cursor):
    inf = give_info(cursor)
    global infs
    if inf == "":
        infs = "No Camp Available on today's date"
    else:
        infs = inf


#
conn = mysql.connector.connect(
    user='root', password='', host='localhost', database='proca213')
cursor = conn.cursor(buffered=True)
infs = ''
check_info(cursor)

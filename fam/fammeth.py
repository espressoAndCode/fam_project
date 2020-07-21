import db_conn
import policy as p
import subprocess
import checksum
import copy
from datetime import datetime


def fam_main():
    # Run File Access Monitor
    run_ui = True
    watchname = ""
    filepath = ""


    # Get all watches from DB
    watchlist = db_conn.get_watches()

    # Select watch definition
    while run_ui:
        for idx, watch in enumerate(watchlist):
            print(f"{idx + 1}. {watch[0]}, {watch[1]}")
        
        sel = input("Please select a watch definition: ")
        print(f"\nSelection is: {watchlist[int(sel) - 1][1]}")
        watchname = watchlist[int(sel) - 1][0]
        filepath = watchlist[int(sel) - 1][1]
        run_ui = False

    # Audit all files in watch path and write audit data to DB
    newest = db_conn.get_latest_time(watchname)

    print(f"Newest: {newest}")

    print(f"P.SEARCH: {p.search['withkey']}")

    run_audit(watchname, newest, p.search['withkey'], p.report['files'], p.refine['rem_xattr'] )

    # Checksum all files in watch path and write checksum data to DB 
    hashes = checksum.walk(filepath)
    db_conn.create_filestate(hashes)

    return


def run_audit(key, newest, search, report, refine):
    print(f"SEARCH: {search}")
    raw_log = read_audit_log(key, search, report, refine)
    text_log = raw_log.stdout.decode()
    text_log = text_log.splitlines()

    for line in text_log:
        splitline = line.split()
       
        
        if len(splitline) == 9 and splitline[0] != '#' and splitline[6].endswith('python3.6') == False: 
            splitdate = parse_date(splitline[1], splitline[2], 0)
            if (newest == None) or (checkdate(splitdate, newest)):
            # if newest == None:
                # print("New")
                print(f"New: {splitline}")
                write_to_db(splitline, key)
        

def write_to_db(record, key):
    data = []   
    # parse to proper format and append to data list
    data.append(parse_date(record[1], record[2], 1))
    data.extend(record[3:8])
    data.append(key)

    # Convert yes/no to 1/0
    if data[3] == 'yes':
        data[3] = 1 
    else:
        data[3] = 0

    # Write to DB
    db_conn.create_data(data)


def read_audit_log(key, search, report, refine):
    print(f"key: {key}, search: {search}, report: {report}, refine: {refine}")
    s = copy.deepcopy(search)
    s.append(key)
    # print("search")
    # print(search)
    p1 = subprocess.run(s, stdout=subprocess.PIPE)
    p2 = subprocess.run(report, input=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.run(refine, input=p2.stdout, stdout=subprocess.PIPE)
    return p3


def parse_date(datestr, timestr, flag):
    datestr += ' ' + timestr
    t = datetime.strptime(datestr, '%m/%d/%Y %H:%M:%S')
    if flag == 0:
        return t
    else:
        return t.strftime('%Y-%m-%d %H:%M:%S')

def checkdate(datea, dateb):
    if datea > dateb:
        return True
    else:
        return False


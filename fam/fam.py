import subprocess
import db_conn
from datetime import datetime


def run_audit(pathname, search, report, refine):
    raw_log = read_audit_log(pathname, search, report, refine)
    text_log = raw_log.stdout.decode()
    text_log = text_log.splitlines()

    for line in text_log:
        splitline = line.split()
        if len(splitline) == 9 and splitline[0] != '#':
            write_to_db(splitline)
        

def write_to_db(record):
    print(f"Record:  {record}")
    data = []   
    # parse to proper format and append to data list
    data.append(parse_date(record[1], record[2]))
    data.extend(record[3:8])

    # Convert yes/no to 1/0
    if data[3] == 'yes':
        data[3] = 1 
    else:
        data[3] = 0

    # Write to DB
    db_conn.create_data(data)


def read_audit_log(pathname, search, report, refine):
    search.append(pathname)
    p1 = subprocess.run(search, stdout=subprocess.PIPE)
    p2 = subprocess.run(report, input=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.run(refine, input=p2.stdout, stdout=subprocess.PIPE)
    return p3


def parse_date(datestr, timestr):
    # date = datestr.replace('/','-')
    datestr += ' ' + timestr
    print(f"Date: {datestr}")
    t = datetime.strptime(datestr, '%m/%d/%Y %H:%M:%S')
    return t.strftime('%Y-%m-%d %H:%M:%S')


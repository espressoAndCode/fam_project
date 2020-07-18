
import fam
import hash
import db_conn
import policy as p


def main():
    filename = "test_watch"
    fam.run_audit(filename, p.search['withkey'], p.report['files'], p.refine['rem_xattr'] )

    # hashfile = "testfile.txt"
    # print(hash.get_hash(hashfile))

    # db_conn.read_data()


    # UI options:
    # 1. Create a watch path
    #     a. Choose parent folder
    #     b. Add flags
    #     c. Add approved users
    # 2. Run File Access Monitor
    #     a. Select watch definition
    #     b. Audit all files in watch
    #         i. Write audit data to DB
    #     c. Checksum all files in watch 
    #         i. Write checksum data to DB 
    # 3. Detect anomalies 
    #     a. Select watch definition
    #     b. Detect illegal access
    #         i.   Read all approved users for selected watch
    #         ii.  Read all items in DB for selected watch 
    #         iii. Compare and flag access by unapproved users
    #         iv.  Display data to user
    #     c. Detect unauthorized file modification
    #         i.   TBD





if __name__ == '__main__':
    main()

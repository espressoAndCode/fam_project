
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




if __name__ == '__main__':
    main()

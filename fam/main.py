from fam import Fam
import hash
import db_conn


def main():
    # filename = "test_watch"
    # watch1 = Fam(filename)
    # print(watch1.read_audit())

    # hashfile = "testfile.txt"
    # print(hash.get_hash(hashfile))

    db_conn.connect()




if __name__ == '__main__':
    main()

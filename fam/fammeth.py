   
import fam
import hash
import db_conn
import policy as p


   # 2. Run File Access Monitor
    #     a. Select watch definition
    #     b. Audit all files in watch
    #         i. Write audit data to DB
    #     c. Checksum all files in watch 
    #         i. Write checksum data to DB 

        # filename = "test_watch"
    # fam.run_audit(filename, p.search['withkey'], p.report['files'], p.refine['rem_xattr'] )

    # hashfile = "testfile.txt"
    # print(hash.get_hash(hashfile))

    # db_conn.read_data()

def test():
    print ("Running File Access Monitor\n")
    return

def fam_main():
    run_ui = True
    while run_ui:
        pfold = input("Please enter the path to the parent folder: ")
        print(f"\nSelection is: {pfold}")

        return
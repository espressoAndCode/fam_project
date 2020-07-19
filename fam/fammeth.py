   
import fam
import hash
import db_conn
import policy as p




def test():
    print ("Running File Access Monitor\n")
    return

def fam_main():
    # Run File Access Monitor
    run_ui = True

    # Get all watches from DB
    watchlist = db_conn.get_watches()

    # Select watch definition
    while run_ui:
        for idx, watch in enumerate(watchlist):
            print(f"{idx + 1}. {watch[0]}, {watch[1]}")
        
        sel = input("Please select a watch definition: ")
        print(f"\nSelection is: {watchlist[int(sel) - 1][1]}")

#     b. Audit all files in watch
#         i. Write audit data to DB
    # filename = "test_watch"
    # fam.run_audit(filename, p.search['withkey'], p.report['files'], p.refine['rem_xattr'] )





#     c. Checksum all files in watch 
#         i. Write checksum data to DB 


    # hashfile = "testfile.txt"
    # print(hash.get_hash(hashfile))







        run_ui = False
    return


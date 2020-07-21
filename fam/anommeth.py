    # 3. Detect anomalies 
    #     a. Select watch definition
    #     b. Detect illegal access
    #         i.   Read all approved users for selected watch
    #         ii.  Read all items in DB for selected watch 
    #         iii. Compare and flag access by unapproved users
    #         iv.  Display data to user
    #     c. Detect unauthorized file modification
    #         i.   TBD
import db_conn

def anom_main():
    # Run File Access Monitor
    run_ui = True
    watchname = ""
     


    # Get all watches from DB
    watchlist = db_conn.get_watches()
    print("\nDetect Unauthorized Access")
    print("---------------------------\n")

    # Select watch definition
    while run_ui:
        for idx, watch in enumerate(watchlist):
            print(f"{idx + 1}. {watch[0]}, {watch[1]}")
        
        sel = input("Please select a watch definition: ")
        # print(f"\nSelection is: {watchlist[int(sel) - 1][1]}")
        watchname = watchlist[int(sel) - 1][0]
        run_ui = False

    print(f"Watch selected: {watchname}")
    print("Performing database query.")
    logs = db_conn.read_data(watchname)
    print(f"Logs: {logs}")

    return
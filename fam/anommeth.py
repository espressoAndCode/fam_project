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
    print("Performing database query.\n")
    logs = db_conn.read_data(watchname)

    unauth = parse_logs_unauth(logs)

    if len(unauth) == 0:
        print("\nNo unauthorized file access detected")
    else:
        print("\nUnauthorized File Access")
        print("---------------------------\n")
        for item in unauth:
            if item[3] == 1:
                print(f"User: {item[5]} SUCCESSFULLY ACCESSED {item[1]} at {item[0].strftime('%Y-%m-%d %H:%M:%S')}.")
            else:
                print(f"User: {item[5]} FAILED TO ACCESS {item[1]} at {item[0].strftime('%Y-%m-%d %H:%M:%S')}.")
    return


def parse_logs_unauth(logs):
    auth_users = []
    unauth_events = []
    # changed_files = []

    print("The authorized users are:\n")
    for user in logs['users']:
        print(user[0])
        auth_users.append(user[0])

    for event in logs['events']:
        if event[5] not in auth_users:
            unauth_events.append(event)

    return unauth_events
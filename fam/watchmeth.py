import db_conn


def test():
    print ("Creating watch path\n")
    return

    # 1. Create a watch path
    #     a. Choose parent folder
    #     b. Add approved users

def watch_main():
    run_ui = True
    more_users = True
    watchname = ""
    pfold = ""
    users = []

    while run_ui:
        watchname = input("Please enter the watcher name: ")
        print(f"\nSelection is: {watchname}")

        pfold = input("Please enter the path to the parent folder: ")
        print(f"\nSelection is: {pfold}")

        while more_users:
            user = input("Please enter a user. Enter q when done: ")
            if user == 'q':
                more_users = False
            else:
                users.append( (watchname, user ))

        print(f"\nUsers: {users}")

        run_ui = False

    # write files to DB
    db_conn.create_watch(watchname, pfold)
    db_conn.create_users(users)

    return

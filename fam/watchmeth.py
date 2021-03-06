import db_conn
import subprocess


    # 1. Create a watch path
    #     a. Choose parent folder
    #     b. Add approved users

def watch_main():
    run_ui = True
    more_users = True
    watchname = ""
    pfold = ""
    users = []

    print("\nCreate a Watch Definition")
    print("---------------------------\n")

    while run_ui:
        watchname = input("Please enter the watcher name: ")
        print(f"\nSelection is: {watchname}")

        pfold = input("Please enter the path to the parent folder: ")
        # print(f"\nSelection is: {pfold}")

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
    success = audit_init(watchname, pfold)

    if success == 0:
        print(f"Watch process {watchname} is now running.")
    else:
        print(f"There was a problem, {watchname} is NOT running.")

    return


#####DON'T FORGET TO ADD THE WATCH TO AUDITD!!!!!!!
def audit_init(watchname, pfold):
    # cmd1 = ['sudo', 'auditctl', '-D']
    cmd2 = ['sudo', 'auditctl', '-w', pfold, '-k', watchname]
    print(f"cmd = {cmd2}")
    # subprocess.run(cmd1)
    p1 = subprocess.run(cmd2)

    return p1.returncode


import db_conn
import subprocess


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
    success = audit_init(watchname, pfold)

    if success == 0:
        print(f"Watch process {watchname} is now running.")
    else:
        print(f"There was a problem, {watchname} is NOT running.")

    return


#####DON'T FORGET TO ADD THE WATCH TO AUDITD!!!!!!!
def audit_init(watchname, pfold):
    cmd = ['sudo', 'auditctl', '-w', pfold, '-k', watchname]
    print(f"cmd = {cmd}")
    p1 = subprocess.run(cmd)

    return p1.returncode


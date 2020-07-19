
def test():
    print ("Creating watch path\n")
    return

    # 1. Create a watch path
    #     a. Choose parent folder
    #     b. Add flags
    #     c. Add approved users

def watch_main():
    run_ui = True
    more_flags = True
    more_users = True
    pfold = ""
    flags = []
    users = []

    while run_ui:
        pfold = input("Please enter the path to the parent folder: ")
        print(f"\nSelection is: {pfold}")

        while more_flags:
            flag = input("Please enter a flag. Enter q when done: ")
            if flag == 'q':
                more_flags = False
            else:
                flags.append(flag)

        print(f"\nFlags: {flags}")

        while more_users:
            user = input("Please enter a user. Enter q when done: ")
            if user == 'q':
                more_users = False
            else:
                users.append(user)

        print(f"\nUsers: {users}")

        run_ui = False

        # call internal methods here

    return

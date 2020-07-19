    # 3. Detect anomalies 
    #     a. Select watch definition
    #     b. Detect illegal access
    #         i.   Read all approved users for selected watch
    #         ii.  Read all items in DB for selected watch 
    #         iii. Compare and flag access by unapproved users
    #         iv.  Display data to user
    #     c. Detect unauthorized file modification
    #         i.   TBD

def test():
    print ("Detecting anomalies\n")
    return


def anom_main():
    run_ui = True
    while run_ui:
        pfold = input("Please enter the path to the parent folder: ")
        print(f"\nSelection is: {pfold}")

        return
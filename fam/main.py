import anommeth, watchmeth, fammeth 


def main():
    run_ui = True
    while run_ui:
        print("1. Create a watch path")
        print("2. Run File Access Monitor")
        print("3. Detect anomalies")
        print("9. Exit")
        ipt = input("Please enter a numeric selection: ")
        print(f"\nSelection is: {ipt}")

        if ipt == "1":
            create_watch()
        elif ipt == "2":
            run_fam()
        elif ipt == "3":
            det_anom()
        elif ipt == "9":
            print("Exiting\n")
            run_ui = False
        else:
            print("Please enter a valid selection\n")

def create_watch():
    watchmeth.test()
    return


def run_fam():
    fammeth.test()
    return


def det_anom():
    anommeth.test()
    return


if __name__ == '__main__':
    main()

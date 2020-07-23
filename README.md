# File Access Monitor
## CPSC6240

### Description

The File Access Manager is a program that leverages the Linux `auditd` process to create actionable logs that will assist system administrators in identifying unauthorized file access and modifcation. The process is based on a file system where user authorization is tracked based on file sub-trees. The program allows the admin to whitelist users for file access to any recursive directories or files beneath the specified root. The process is:

1.	Create a file access management watcher for a given sub-tree. This will monitor all file system access below that folder and monitor all file modification through checksum logs.

1.  Assign authorized users for the watcher.
    
1.	Run a baseline checksum.

1.	Run the file watcher daemon.

## Setup

This project is tested on Ubuntu 18.04. Your mileage may vary on other versions of Linux. 

### Install `auditd`

    sudo apt update
    sudo apt install auditd


This project requires Python3 with the Pip3 package manager installed. If you aren't already set up, here's a good overview:
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart


### Clone the repo

    $ https://github.com/espressoAndCode/fam_project.git

### Navigate into the project folder

    $ cd fam_project

### Install dependencies

    $ pip3 install -r requirements.txt

### Database

You will also need a MySql database. I used the Clemson Buffet service for a near zero-configuration instance. If you are off campus you will need to connect with the Cisco AnyConnect VPN. Create a MySQL instance and record the credentials.

Database build files are located in the `DBbuilders` directory. You will need to run the CreateTables script. Once you are connected to your MySQL instance, navigate to the `DBbuilders/` directory and run:

    source CreateTables.sql

This will build the tables according to the correct schema.

The File Access Manager program will need to connect to the database as well. Connection credentials are accessed in the `db_conn.py` file, and you can connect by simply adding the credentials to your `.bashrc` file as environment variables using this format:

    export FAM_HOST="hostname"
    export FAM_USER="username"
    export FAM_PASS="DBpassword"
    export FAM_DB="DBname"

## Operation

To run the program, navigate to the `/fam_project/fam` directory and enter:

    $ python3 main.py

Be sure to follow the prompts, you may be required to enter your `sudo` password during the process.

    1. Create a watch path
    2. Run File Access Monitor
    3. Detect anomalies

The segments build on each other. You must first create a watch path, then you can run the File Access Monitor on one of those watches. You only need to create the watch once, and each watch must have a unique name. The watch path is the full path to the top level directory, ie:

    /home/user/dir1/dir2/

In this case, everything in `dir2` and below will be tracked with the watcher. Subsequent runs of the same watcher will only add items to the database that occurred since the last run.
 
 You should run the File Access Monitor for a watch immediately upon creating it in order to get a clean baseline. Any subsequent activity in that file tree will be tracked as long as the watcher is running.

 ## * Watchers do not persist across restarts in this demo implementation.

Once some activity has occurred, you can run the anomaly detector for the watch file. Please note that users are tracked by Auid (audit userID), so if you change user using the `su` command, you will still be tracked by your real user ID. In order to observe the correct operation of the anomaly detector, log out and back in as another user. The actual user ID will then be correctly reflected in the logs.


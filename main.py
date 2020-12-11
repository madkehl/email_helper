from emails import full_path
import pandas as pd
from send_emails import login_pitt, open_outlook

ids = pd.read_csv('/users/madke/downloads/AAPECS Recontacts.csv')

def main(ids):
    results = full_path(ids)
    drive = login_pitt()
    drive2 = open_outlook(drive)

if __name__ == "__main__":
    main()

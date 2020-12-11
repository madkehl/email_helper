from emails import full_path
import pandas as pd
from send_emails import login_pitt, open_outlook, new_message

ids = pd.read_csv('/users/madke/downloads/AAPECS Recontacts.csv')
subject = 'Mental Health and Covid-19 Follow-up'


def main(df):
    results = full_path(df)
    driver = login_pitt()
    driver = open_outlook(driver)
    for index, row in results.iterrows():
        driver = new_message(driver, row['email'], row['template'], subject)


if __name__ == "__main__":
    main(ids)

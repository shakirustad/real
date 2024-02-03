#importing the required libraries
import gspread
# import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('first-413209-b6139f9d9b57.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('commentary data')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get the total number of columns
sheet_instance.col_count
## >> 26
print(sheet_instance.col_count)

# get the value at the specific cell
print(sheet_instance.cell(col=2,row=4))
## >> <Cell R2C3 '63881'>

# get all the records of the data
records_data = sheet_instance.get_all_records()

# view the data
print(records_data)

# add a sheet with 20 rows and 2 columns
sheet.add_worksheet(rows=20,cols=2,title='runs')

# get the instance of the second sheet
sheet_runs = sheet.get_worksheet(1)

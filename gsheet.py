import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# SETUP
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("sheetsKEY.json", scopes) #access the json key
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Reminders")
sheet = sheet.sheet1


# Function for creating a reminder
def create(Title, Date, Type=None):
    
    row_index = 1
    content = "Title"
    
    for i in range(2,1000):
        if sheet.cell(i,1).value == None:
            row_index = i
            print("row index set to " + str(row_index))
            break
    
    #Create id
    ids = sheet.col_values(4)[1:]
    id = None
    for i in range(1,len(ids)+1):
        if str(i) not in ids:
            id = i
            break
    if id == None and len(ids) not in ids:
        id = len(ids)+1
    else:
        print("This should not have happened!")
    
    #Format Type
    if Type == None:
        Type = "None"

    #Create the reminder
    sheet.update_cell(row_index, 1, Title)
    sheet.update_cell(row_index, 2, Type)
    sheet.update_cell(row_index, 3, Date)
    sheet.update_cell(row_index, 4, id)

    return("I have created a reminder!")

#create("test05", "2022-09-15")
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


def show(Nope=None, type=None):
    '''Shows the current Reminders'''
    '''Show a table of the reminders'''
    
    # Extract table from google Sheet
    Table = {}
    Table["Title"] = sheet.col_values(1)[1:]
    Table["Type"] = sheet.col_values(2)[1:]
    Table["Date"] = sheet.col_values(3)[1:]
    Table["id"] = sheet.col_values(4)[1:]

    myDF = pd.DataFrame(Table)

    #Filter out the undesired types. Format DataFrame
    if type != None:
        #User wants opposite of type
        if Nope == True:
            myDF = myDF[myDF.Type != type]
        
        #User wants type
        elif Nope == False or Nope == None:
            myDF = myDF[myDF.Type == type]
        else:
            return("I don't understand. I should not have gotten here.")
        #myDF = myDF[myDF.Type ==]
    #else: show everything

    #Check row length
    if len(myDF.index) > 10:
        return(["Row count was > 10: will return only 10 rows.", myDF.head(10)])
    else:
        return(myDF.head())
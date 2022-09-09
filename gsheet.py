import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

import datetime

# SETUP
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("sheetsKEY.json", scopes) #access the json key
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Reminders")
sheet = sheet.sheet1


# GET REMINDERS
def get_reminders():
    '''This function retrieves the reminders'''
    Table = {}
    Table["Title"] = sheet.col_values(1)[1:]
    Table["Type"] = sheet.col_values(2)[1:]
    Table["Date"] = sheet.col_values(3)[1:]
    Table["id"] = sheet.col_values(4)[1:]

    myDF = pd.DataFrame(Table)

    return(myDF)

# SEND REMINDERS
def send_reminders():
    '''This function looks through the table of reminders'''
    '''and decides weather or not to send reminders'''

    myDF = get_reminders()

    messages = [] #Fill up with reminders for the user
    today = datetime.datetime.today()
    today = datetime.datetime(today.year, today.month, today.day, 12, 0)

    for i in myDF.T: #Cycle through row indexes (i is a row index)
        #print(myDF[i]["Title"])

        DOB = datetime.datetime.strptime(myDF.T[i]["Date"], "%Y-%m-%d") #Date Of Birth
        born_this_year = datetime.datetime(today.year, DOB.month, DOB.day, 12, 0)
        difference = born_this_year - today
        
        #print(str(difference.days) + " and the type: " + str(type(difference.days)))
        
        #if myDF.T[i]["Title"] == "Barney":
            #print("Diff: " + str(difference))

        ##Check 30 days
        if(difference.days <= 30 and difference.days > 10):
            messages.append("It is " + myDF.T[i]["Title"] + "'s birthday in " + str(difference.days) + " days!")
            #print("It is " + myDF.T[i]["Title"] + "'s birthday in " + str(difference.days) + " days!")
            #await channel.send("It is " + i[0] + "'s birthday in " + str(difference.days) + "days!")
        
        ##Check 10 days
        if(difference.days <= 10 and difference.days > 0):
            messages.append("It is " + myDF.T[i]["Title"] + "'s birthday in " + str(difference.days) + " days!")
            #print("It is " + myDF.T[i]["Title"] + "'s birthday in " + str(difference.days) + " days!")
            #await channel.send("It is " + i[0] + "'s birthday in " + str(difference.days) + "days!")

        ##Check today
        if(DOB.day == today.day and DOB.month == today.month):
            messages.append("It is " + myDF.T[i]["Title"] + "'s birthday today!")
            #print("It is " + myDF.T[i]["Title"] + "'s birthday today!")
            #await channel.send("It is " + i[0] + "'s birthday today!")
    
    return messages

#send_reminders()


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

    #Retrieve reminders from the google sheet
    myDF = get_reminders()

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
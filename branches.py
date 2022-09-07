import re
import datetime
import gsheet

'''
This file contains functions for the specific branches and sub-brances
that represent possible uses of the bot.
'''

# Iterator wrapper
def advance(commands):
    # Function used to go through the commands, and returning None when reaching end
    try:
        return next(commands)
    except StopIteration:
        return None

# Function to gather up remaining commands and notify the user
def unknown_commands(current_command, commands):
    unknowns = []            
    while current_command != None:
        unknowns.append(current_command)
        current_command = advance(commands)
    
    if len(unknowns) > 1:
        return("Multiple unknown commands: " + "\"" + "\", \"".join(unknowns) + "\"")
    else:
        return("Unknown command: " + "\"" + unknowns[0] + "\"")


# MASTER node
def bot(text):
    #Use this function to divide the possible actions of the bot into functions.
    
    #Split up the commands and create an iterator
    commands = iter(text.split(" "))
    current_command = advance(commands) #Go to first command
    
    if current_command != "bot":
        return("bot node master was incorrectly called. First command should be \"bot\", not " + "\"" + current_command + "\"")
    
    #Next command
    current_command = advance(commands)

    if current_command == None:
        return("Missing needed commands after \"bot\"")
    
    # Look for a branch

    #REMIND branch
    if current_command == "remind":
        return remind(commands)
    
    # PLOT branch
    if current_command == "plot":
        return plot(commands)
    
    # HELLO branch
    if current_command in ["hello", "hi", "Hello", "HELLO", "HI", "whatup", "goodday", "greetings"]:
        return hello(commands)
    
    # HELP branch
    if current_command == "help":
        #Extend here
        help_message = "This bot has the following sub branches:\n"
        help_message += "remind: creates a reminder\n"
        help_message += "plot: plots a graph\n"
        help_message += "help: prints this message"
        return(help_message)
    
    return(unknown_commands(current_command, commands))


# REMIND branch
def remind(commands):
    #Go to next command (after "remind")
    current_command = advance(commands)

    # Missing needed commands
    if current_command == None:
        return("Missing needed commands")

    # REMOVE REMINDER sub-branch
    if current_command == "remove":
        #Extend here
        return("I will remove")
    
    # SHOW REMINDER sub-branch
    if current_command == "show":
        current_command = advance(commands)
        
        #return(gsheet.show())
        
        return("I will show")

    # CREATE REMINDER sub-branch
    if re.search("(\d\d\d\d-)?\d\d-\d\d", current_command) or current_command == "today":
        #Contains date, title (in those positions)
        remind_variables = ["2022-09-02", "default title"]

        #Extract DATE
        if current_command == "today":
            remind_variables[0] = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            remind_variables[0] = current_command
        
        current_command = advance(commands)

        #Extract Title
        if current_command == None:
            return("Missing title for reminder")
        else:
            remind_variables[1] = current_command

        #Deal with the rest of the create reminder branch

        #HERE is where we should do the actual creating of the reminder
        gsheet.create(remind_variables[1], remind_variables[0], "None")

        # Send information back so that bot can notify user
        return("I have created a reminder on " + remind_variables[0] + " called " + remind_variables[1])
    
    # REMINDER HELP Sub-branch
    if current_command == "help":
        #Extend here
        help_message = "The remind branch has the following sub branches:\n"
        help_message += "remove\n"
        help_message += "show\n"
        help_message += "create"
        return(help_message)
    
    # DEALING WITH UNKNOWN COMMANDS
    #at this point, anything useful should have been caught already
    return unknown_commands(current_command, commands)


# PLOT branch
def plot(commands):
    #Go to next command (after "plot")
    current_command = advance(commands)

    return("I will plot")


# GREETING branch
def hello(commands):
    #Go to next command (after "hello" or "hi" etc)
    current_command = advance(commands)

    return("Hello!")


# For continuous testing
#input_message = ""
#print("Type \"exit testing\" to exit program.")
#while input_message != "exit testing":
#   input_message = input(">>")
#    print(bot(input_message))


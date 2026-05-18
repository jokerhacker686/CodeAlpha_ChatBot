import datetime as dt
import os
import pyjokes as joke
import json as js

# Current Date Function 
def DATE():
    timeraw = dt.date.today()
    date = timeraw.strftime("%d-%m-%Y")
    return date

# Current Time Function 
def TIME():
    timeraw = dt.datetime.now()
    Time = timeraw.strftime("%H:%M:%S")
    return Time

# Clear Display Function
def clear():
    os.system('clear')

# Jokes Finction
def jokes():
    return joke.get_joke('en','all')



class Command:

    # All Data store here
    def __init__(self):

        # Store Command List 
        self.Command_list = {
            "date" : DATE,
            "time" : TIME,
            "joke" : jokes,
            "clear" : clear,
            "history" : self.History,
            "add" : self.Add,
            "help" : self.Show_Command_All,
            "exit" : "exit"
        }

        # store Command History 
        self.Command_History = []
        pass
 
    # Add Command List 
    def Add(self):
        print("=== ADD Function Name ===\n")
        Function_Name = input("Enter Function Name :- ")
        Function_Value = input("Enter Funtion Value :- ")
        self.Command_list[Function_Name.lower()] = Function_Value.lower()

    # Call Function 
    def Call(self,Function_Call):
        try:
            self.Command_History.append(Function_Call)
            Output = self.Command_list.get(Function_Call)()
            return Output
        except:
            return "Command Not Exit"
    
    # Show Command List 
    def Show_Command_All(self):
        print(f"ChatBot :- {"list"}")
        for ind,keys in enumerate(self.Command_list.keys() , start=1):
            print(f"{ind} {keys}")
        print()

    # Show History list
    def History(self):
        print(f"ChatBot :- {"history"}")
        for index,single in enumerate(self.Command_History, start=1):
            print(f"{index} : {single}")
        print()




if __name__ == "__main__":
    Co = Command()
    Output = "Welcome" 
    print(f"ChatBot :- {Output}")
    
    while True:

        Input_Call = input("Me :- ")
        Input_Call = Input_Call.lower()
        if Input_Call == "exit":
            break
        else:
            Output = Co.Call(Input_Call) 
            print(f"ChatBot :- {Output}") 
        
          
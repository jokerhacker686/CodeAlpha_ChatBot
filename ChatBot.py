


def welcome():
    Name = "vikram"
    print(f"Welcome {Name}  sir\n")

class Command_Class:
    def check(slef):
        print("check")



    
def Function_Call(Function_Name):
   print("Function_Call")


def Input():
   print("Input")


def Print(Output):
   print("Print")



def heart():
    welcome()
    cd = Command_Class()
    while True:
        input = Input()
        Function_Name = cd.check()
        Output = Function_Call(Function_Name)
        Print(Output)
        break


 
    

if __name__ == "__main__":
    heart()
    # cd.check()
    
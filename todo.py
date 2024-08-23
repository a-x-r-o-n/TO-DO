from module import *

while True:

    displayList()

    stateChange = input("\n\nAvailable action for the current version are \n\n\'add\' for add a tak to your list\n\'cross\' for Strick the finished task\n\n enter action: ").lower()
    if stateChange == 'add':

        addList()
        
    elif stateChange == 'cross':
        
        crossTask()
        
    elif stateChange == 'quit':
        
        print("Thank you")
        break
        
    
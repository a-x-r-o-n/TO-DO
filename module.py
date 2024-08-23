work = []
personal = []
general = []
DBstack = [work,general,personal]

def displayList():
    
    print("Your TO-DO List")

    if len(work) == 0 and len(personal) == 0 and len(general) == 0:

        print("\n\n!! LIST EMPTY !!")
    else:
        for i in DBstack:
            wi,gi,pi = 0,0,0
            for j in i:
                if i == work:
                    wi += 1
                    print(f"WORK: {wi}) ",end = '')
                elif i == general:
                    gi += 1
                    print(f"GENERAL: {gi}) ",end = '')
                elif i == personal:
                    pi += 1
                    print(f"PERSONAL: {pi}) ",end = '')
                print(j)
def addList():
    Category = input("\n\nWORK  |  GENERAL  |  PERSONAL\n\nENTER CATEGORY: ").lower()
    if Category == "work":
        work.append(input("\n\nenter Task: "))
        
    elif Category == "general":
        general.append(input("\n\nenter Task: "))
        
    elif Category == "personal":
        personal.append(input("\n\nenter Task: "))
def crossTask():
    
        Category = input("\n\nWORK  |  GENERAL  |  PERSONAL\n\nENTER CATEGORY: ").lower()
        taskId = int(input("enter TaskID: "))
        if Category == "work":
            work.pop(taskId-1) 
        elif Category == "general":
            general.pop(taskId-1)
        elif Category == "personal":
            personal.pop(taskId-1)

tblTodo= ["Clean bed", "Change computer parts", "Develop a functioning potateo"]

def menu():
  print("[1] Create List")
  print("[2] Update List")
  print("[3] Delete List")
  print("[4] Exit The program")
  chooseTodo()
  
def createTodo():
  print(tblTodo)


def updateTodo():
  print("update")
  #So what I need to do is create if statment that will basiclly show that vallue is true
  #You can do it in diffrent ways bool and ect...

def deleteTodo():
  print("Print delete")
 # tblTodo.remove()
  #print(tblTodo)

def exitTodo():
  
  exit()

def chooseTodo():
  #choiceX = input("Please 1select what Todo action y1ou would like to have? ") 
 
  x = int(input("Please select what action you would like to do "))
  while x != 0:
    if x == 1:
      createTodo();
    elif x == 2:
      updateTodo()
    elif x == 3:
      deleteTodo()
    elif x == 4:
      exitTodo()
    else:
      print("Error please input correct value and choose a following option")

 
 
          

    
  

    
    
    
    #I can add way to implement in for loop.
    #Todo need to cadd way of adding or accessing other functions...

menu()
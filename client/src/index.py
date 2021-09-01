
tblTodo= ["Clean bed", "Change computer parts", "Develop a functioning potateo"]

def menu():
  print("[1] Create List")
  print("[2] Update List")
  print("[3] Delete List")
  print("[4] Exit The program")
  chooseTodo()
  
#Completed
def createTodo():
  numAmmountList = 0
  for y in tblTodo:
    numAmmountList+=1
    print("(",numAmmountList,")",("{") , y ,("}"))
  createInput = input("Input value: ")
  tblTodo.append(createInput)
  print(tblTodo)
  menu()


def updateTodo():
  numAmmountList = 0
  for y in tblTodo:
    numAmmountList+=1
    print("(",numAmmountList,")",("{") , y ,("}"))
#Ducking Fix this I cam't fox ot tored and ducking fed up....
  choiceSelected = int(input("Please select what you want to update! "))
  if tblTodo[y] == choiceSelected:
    print("Choices selected do want to change it (Yes or No)")
    inp= input().lower()
    if inp == "yes":
      tempChange = input("Please input what you wanted to change")
      tblTodo[y] = tempChange
      print("Example")
    elif inp == "no":
      updateTodo()


        
  
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
 
  x = input("Please select what action you would like to do ")
  while x != 0:
    if x == "1":
      createTodo();
      break
    elif x == "2":
      updateTodo()
      break
    elif x == "3":
      deleteTodo()
      break
    elif x == "4":
      exitTodo()
    else:
      print("Error please input correct value and choose a following option")
      
      

 
 
          


    
  

    
    
    
    #I can add way to implement in for loop.
    #Todo need to cadd way of adding or accessing other functions...

menu()
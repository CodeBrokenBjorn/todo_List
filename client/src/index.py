
tblTodo= ["Clean bed", "Change computer parts", "Develop a functioning potateo"]



  
def createTodo(tblTodo):
  print(tblTodo)


def updateTodo(tblTodo):
  #So what I need to do is create if statment that will basiclly show that vallue is true
  #You can do it in diffrent ways bool and ect...

def deleteTodo(removeVal):
  tblTodo.remove(removeVal)
  print(tblTodo)

def exitTodo(tblTodo):
  exit()

def chooseTodo():
  tempChoose = (createTodo, updateTodo, deleteTodo)
  x = input("Please select what Todo action you would like to have? ")
  for x in tblTodo:
    print(x)
    removeVal = x
    #Todo need to cadd way of adding or accessing other functions...
  
  
    


      



chooseTodo()
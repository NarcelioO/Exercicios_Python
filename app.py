#functions
def collatz(Number):
  
  if Number % 2 == 0:
    return Number / 2 
  elif Number % 2 ==1:
    return 3 * Number + 1
 #erros   
""" try:
  print(collatz(Number = int(input("Digite um numero: "))))
except:
  print("O valor inserido deve ser um inteiro")
 """
spam = ['1', '2', '3', '4']


""" catNames = []
while True:
  print('Enter the name of cat'+ str(len(catNames) + 1) + '(Or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  catNames += [name]
print("cat names:")
for name in catNames:
  print(''+ name)
 """


""" supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
  print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print(type(supplies))
 """


""" myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
  print('I do not have a pet named ' + name)
else:
  print(name + ' is my pet.')
 """
""" 
pets = ['fat', 'black','loud']

size, color, disposiion = pets

print(size, color, disposiion) """

pets = ['fat', 'black','loud']

""" pets.append(input())
while True:
  print('Enter the name of pet'+ str(len(pets) + 1) + '(Or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  pets.append(name)
print("cat names:")
for name in pets:
  print(''+ name)
#append() add the argument at the of list.
#insert() add the argument in any position list, passing the index as the first argument

 """
""" tasks = []

def addTask():
  task = input('-----Add a taks: ')
  tasks.append(task)
  print('task added!')

def listTasks():
  if not tasks:
    print(' !!! no one task !!!')
  for i, task in enumerate(tasks, 1):
    print(f"{i}.{task}")
    
def editTask():
  listTasks()
  choise = int(input('------Escolha numero da Task: '))
  newValue = input('Digite o novo valor:')
  if 0 < choise <= len(tasks):
    tasks[choise - 1] = newValue
    listTasks()
  else:
    print("digite uma task valida: ")
  print("task updated")

def removeTask():
    listTasks()
    num = int(input("----Escolha task para remover: "))
    if 0 < num <= len(tasks):
      remove = tasks.pop(num-1)
      print(f'tarefa{remove}removida')


while True:
  print("\n 1.adcionar tarefa\n 2.Listar tarefas\n 3.Editar Tarefa \n 4.Remover tarefa \n 5.sair")
  choise = input('Escolha a operação: ')
  if choise== '1':
    addTask()
  elif choise == '2':
    listTasks()
  elif choise == '3':
    editTask()
  elif choise == '4':
    removeTask()
  elif choise == '5':
    break
  else:
    print('opção invalida') 
 """



""" 
name = ''
password=''
while not name:
  print('Who are you?')
  name = input()
while password != 'swordfish':
  print(f'Hello ' + name + ', what is the password?')
  password = input()

print('Access granted') """

""" 
import random

def getAnswer(answerNumber):
  if answerNumber == 1:
    return 'It is certain'
  elif answerNumber == 2:
      return 'It is decidedly so'
  elif answerNumber == 3:
      return 'Yes'
  elif answerNumber == 4:
    return 'Reply hazy try again'
  elif answerNumber == 5:
    return 'Ask again later'
  elif answerNumber == 6:
    return 'Concentrate and ask again'
  elif answerNumber == 7:
    return 'My reply is no'
  elif answerNumber == 8:
    return 'Outlook not so good'
  elif answerNumber == 9:
    return 'Very doubtful'
  
r = random.randint(1, 9)

fortune = getAnswer(r)

print(fortune) """

##Tuple

print(type(('hello')))


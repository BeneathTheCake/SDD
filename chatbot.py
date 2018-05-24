import time
import json

def inputData(orders):
  while True:
    name = input('Name? ');
    if name =='':
        break
    choice = input ('Menu Choice? ')
    orders[name]=choice
  return orders
    
##Store it in a file
def storeData(orders):
    with open('data.txt', 'w') as f:
      json.dump(orders, f)

  
## Get it from file
def getData():
  with open('data.txt', 'r') as f:
      orders = json.load(f)

  return orders
## Display contents
def displayData(orders):
  print(orders);

##mainline
storeData(inputData(orders))
displayData(getData())


time.sleep(1);
print("Welcome to the SushiGo Website!");
print('')
time.sleep(1);
print("I'm Gobot, your personal online assistant.");
print('');
time.sleep(1);
print("You can order Sushi through me and skip the hassel of searching yourself.");
print('')
time.sleep(1);
process = input('What would you like to do?: ');
commands = ["i want food", "i want to order food!"];

while process not in commands:
  time.sleep(1);
  print("I'm sorry, I don't quite understand");
  time.sleep(1);
  process = input('What would you like to do?: ');

time.sleep(1.5);
name = input('Before we begin, may I please have your name?: ');

while 'my name is' not in name:
  time.sleep(1.5);
  print("I'm sorry, I don't quite understand.");
  time.sleep(1.5);
  name = input("May I please have your name?: ");

else:
  name = name.replace('my name is', '');
  


time.sleep(1.5);
confirm = input('So your name is' + name + '? ');


while confirm == 'no':
  time.sleep(1);
  print('Sorry!');
  time.sleep(1)
  name = input('Please enter your correct name: ');
  name = name.replace('my name is', '');
  confirm = input('So your name is' + name + '? ');
  
  
  
  

else:
  name = name.replace('My name is', '');
  print('Cool!' + ' ' + name + '... I like the sound of that name!');


print('Now we can move onto the menu items.')

decision = input('Would you like to look at the MENU?: ');

if decision == 'yes':
     print('---------- MENU -----------');
     print('');
     print('           Sushi           ');
     print('      Meatlovers Pizza     ');
     print('      Supreme Pizza        ');
     print('      Pepperoni Pizza');
     print('      Margharita Pizza');
     print('      Cookie-Dough Pizza');
     print('');


    
pizza = ['Meatlovers Pizza', 'Supreme Pizza', 'Pepperoni Pizza', 'Margharita Pizza', 'Cookie-Dough Pizza']

ordercart = []
order = []



while True:
    while order != 'done':
      order = input('What would you like to ORDER?: ');
      if order in pizza:
       ordercart.append(order);
       print('CHECKING ITEM....');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.75);
       print('SAVING ORDER.....');
       time.sleep(0.5)
       print('.................');
       time.sleep(0.5)
       print('.................');
       time.sleep(0.75)
       print('SAVE SUCCESSFUL');
       print("Here is your order so far:" + str(ordercart));
       print('When you have finished ordering, say done.');
      elif order != 'done':
       print('CHECKING ITEM....');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.5);
       print('.................');
       time.sleep(0.75);
       print('ERROR............');
       print('This item is NOT on the MENU');



    if len(ordercart) >= 3:
     confirm = input('Have you finished ordering?: ');
     if confirm == 'no':
       order = 0
     else:
       print('');
       print('');
       print('');
       print('-------------------------------------------------------------');
       time.sleep(1);
       print('FINAL ORDER');
       time.sleep(0.5);
       print(name + ':' + ' ' + ' ' + str(ordercart));
       print('-------------------------------------------------------------');

    if len(ordercart) < 3:
      print('Unfortunately, you have not ordered enough items for DELIVERY');
      order = 0
      
      
      
    else:
      break
      

  
    
     
  

       
       
      
      
      
      
      

    





    



  

 

  


  
     








    
      
  
             


  

    
        
              
  
   

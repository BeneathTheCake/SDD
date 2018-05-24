import time
import json



time.sleep(1);
print("Welcome to the SushiGo Website!");
print('')
time.sleep(1.5);
print("I'm Gobot, your personal online assistant.");
print('');
time.sleep(1.5);
print("You can order Sushi through me and skip the hassel of searching yourself.");
print('')
time.sleep(1.5);
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
  time.sleep(0.5);
  print('Sorry!');
  time.sleep(0.5)
  name = input('Please enter your correct name: ');
  name = name.replace('my name is', '');
  confirm = input('So your name is' + name + '? ');  


else:
  name = name.replace('my name is', '');
  print('Cool!' + ' ' + name + '... I like the sound of that name!');


with open('ordering.txt') as json_file:
  json.load(json_file)
  if name in json_file:
    print('OH');

print('Now we can move onto the menu items.')

decision = input('Would you like to look at the MENU?: ');

if decision == 'yes':
     print('-------------------------------------- MENU ---------------------------------------');
     print('');
     print('                                       FOOD');
     print('')
     print('                              California Roll: $3.40');
     print('      - An American style roll created in California for the American palate.');
     print('')
     print('                                    Maki: $4.40');
     print('                      - Rice and filling wrapped in seaweed');
     print('')
     print('                                   Nigiri: $5.35');
     print('               - A topping, usually fish, served on top of sushi rice');
     print('')
     print('                                  Sashimi: $11.65');
     print('                   - Fish or Shellfish served alone. (No Rice)');
     print('')
     print('                                   Tobiko: $7.40');
     print('               - Roe of flying fish and is usually a bright orange.');
     print('')
     print('                                    Poke: $6.50');
     print('                                 - Raw fish salad.');
     print('')
     print('')
     print('                                       DRINKS');
     print('')                                    
     print('                                   Coca-Cola: $2.50');
     print('')
     print('                                     Fanta: $2.45');
     print('')
     print('                                 Orange Juice: $2.00');
     print('')
     print('-----------------------------------------------------------------------------------');


    
menu = {
    "california roll" : 3.40,
    "maki" : 4.40,
    "nigiri" : 5.35,
    'sashimi' : 11.65,
    'tobiko' : 7.40,
    'poke' : 6.50,
    'coca-cola' : 2.50,
    'fanta' : 2.45,
    'orange juice' : 2.00,
}


orderlist = []

order = 0
count = 0
for item in menu:
    price = menu[item]
    count += 1
totalcost = 0

totalcount = 0
while True:
    while order != "":
      order = input("What would you like to order?: ").lower().strip()
      if order in menu:
        orderlist.append(order)
        cost = menu[order]
        totalcost = totalcost + cost
        print('CHECKING ITEM.........');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('SAVING ORDER..........');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('SAVE SUCCESSFUL.......');
        time.sleep(1);      
        print(f"Thank you for ordering - {order}, that will cost ${cost}, and your total is now ${totalcost}");
      elif order != '':
        print('CHECKING ITEM.........');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('ERROR DETECTED........');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('......................');
        time.sleep(0.25);
        print('SAVE UNSUCCESSFUL.....');
        time.sleep(1);
        print(f"Unfortunately {order} is not in the Menu...");
        

    if len(orderlist) >= 3:
       orderchoice = input('Have you finished ordering?: ');
       if orderchoice == 'no':
         order = 0
       else:
         break
        

    if len(orderlist) < 3:
       print('Unfortunately you have not ordered enough items for a DELIVERY');
       print('You have only ordered' + ' ' + str(len(orderlist)) + ' item/s.');
       order = 0

jsondata = name[orderlist]


with open('ordering.txt', 'w') as outfile:
  json.dump(jsondata, outfile)
       
print('');
print('');
print('');
print('-------------------------------------------------------------');
time.sleep(1);
print('FINAL ORDER');
time.sleep(0.5);
print("You " + name + ", have ordered " + str(totalcount) + " item/s and your total is now $" + str(totalcost) +".");
print(str(orderlist));
print('-------------------------------------------------------------');










   
    
     
      





    
    



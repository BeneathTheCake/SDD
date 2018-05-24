import json


orders = {
  'andrew' : ['tacos'],
  'noone' : ['bb food', 'mush'],
}

for person in orders:
  choices = orders[person]
  print(f'{person} has ordered:')
  for orderList in choices:
    print('====')
  for item in choices:
    print(item)


with open('orders.txt', 'w') as f:
  json.dump(orders,f)

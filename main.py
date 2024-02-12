import random
x=0
nm=int(input('Enter number of players:'))
lst=[]
dic={}
if nm not in range(2,5):
  print('Invalid user number')
for i in range(0,nm):
  name=input('player name:')
  #lst.append(name)
  dic.update({name:0})
  lst.append(name)
while True:
  j=0
  for k,v in dic.items():
    print('Welcome',k)
    r=input('Press (r) to roll: ')
    if r=='r':
      roll=random.randint(1,6)
      print('You got:',roll)
      v=v+roll
      dic[k]=v
      print('Your total score till now is: ',v)
      j+=1
      if v>=50:
        print('Congratulations',k, 'you won')
        x=1
        break
    else:
      print('Your turn skipped.Please press Enter next time '.upper())
      continue
  if x==1:
    break
print('Thank you for playing')
print('Total ScoreBoard', dic.items())


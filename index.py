nameInput =  (input('what is 1+1? '))
if int(nameInput) == 2:
  print ('You are good at math') 
else:
  print ('Are you sure about that' + '1+1 does not equal ' + nameInput)
  rInput = (int(nameInput) / 2 ) 
  print ('Your answer works for ' + str(rInput) + '+' + str(rInput))
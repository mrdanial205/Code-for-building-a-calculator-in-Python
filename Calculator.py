Alamat = input ('enter your Alamat:')
Number1 =int(input ('enter your 2 Number:'))
Number2 =int(input ('enter your 2 Number:'))
if Alamat == '+':
      print(f'{Number1} + {Number2} = {Number1 + Number2}')
elif Alamat == '*':
      print(f'{Number1} * {Number2} = {Number1 * Number2}')
elif Alamat == '**':
      print(f'{Number1} ** {Number2} = {Number1 ** Number2}')
elif Alamat == '/':
      print(f'{Number1} / {Number2} = {Number1 / Number2}')
elif Alamat == '-':
      print(f'{Number1} - {Number2} = {Number1 - Number2}')
else:
      print('error!')
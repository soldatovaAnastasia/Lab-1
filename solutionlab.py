
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
END = '\u001b[0m'

for i in range(10):
    if i < 3:
         print(f'{YELLOW}{"  " * (15)}{END}')
    if 2 < i < 6:
          print(f'{GREEN}{"  " * (15)}{END}')  
    if i > 6:
        print(f'{RED}{"  " * (15)}{END}') 

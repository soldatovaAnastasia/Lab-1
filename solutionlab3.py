WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(5):
    if i == 0 :
        print(f'{" " * 6}{WHITE}{" " * 9}{END}{" " * 6 }'*2)
    elif i ==1:
        print(f'{" " * 6}{END}{" " * 9}{WHITE}{" " * 3}{END}{" " * 6}{WHITE}{" " * 3}{END}')
    else:
        print(f'{" " * 3}{END}{" " * 15}{WHITE}{" " * 6}{END}')

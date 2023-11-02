plot_list = [[0 for i in range(20)] for i in range(20)]
result = [0 for i in range(20)]

for i in range(20):
    result[i] = i * 2

step = round(abs(result[0] - result[9]) / 9, 1)
print(step)
        
for i in range(20):
    for j in range(20):
        if j == 0:
            plot_list[i][j] = step * (i) + step            
        if j == 10:
            plot_list[i][j] = (9-i)

for i in range(9):
    for j in range(20):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(10):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(20):
        if j == 10:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!'
    print(line)
#print('\t-3  -2  -1      0       1   2   3')
#В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
f = open("class.txt", 'r')
sum = 0
n = 0
for s in f:
    s = s.split()
    d = int(s[2])
    sum +=  d
    n += 1
    if d < 3:
        print(s[0], s[1] , s[2])
f.close()
print('Средний балл %.2f' %(sum/n))
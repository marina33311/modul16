a = {'торт': [["мука","яйца","клубника","сгущенка"], 5, 500],
     'пирожное': [["сахар","яйца","сметана","мед"], 3, 300],
     'маффин': [["изюм","мука","яйца","разрыхлитель"], 2, 200]}
print('Введите, что хотите узнать?(состав, цена, количество, всю информацию, приступить к покупке)  ')
d = input()
if d == 'состав':
    for key, value in a.items():
        print(key, '-', ','.join(value[0]))
if d == 'цена':
    for key, value in a.items():
        print(key, f'- {value[1]}р. за 100гр.')
if d == 'количество':
    for key, value in a.items():
        print(key, f'- {value[2]} гр.')
if d == 'всю информацию':
    for key, value in a.items():
        print(f'\n {key}', '\nСостав:', ",".join(value[0]),
              f'\nЦена: {value[1]}р. за 100гр.', f'\nКоличество: {value[2]} гр.')
else:
    cost = 0
    while True:
        kond = input('Что вы хотите купить? "торт", "пирожное", "маффин" или ' "Введите n для завершения покупок")
        if kond == 'n':
            break
        gram = float(input('Сколько грамм вы хотите купить?'))
        if gram > float(a[kond][2]):
            print('У нас столько нет, выберите другое количество или товар')
            continue
        cost = cost + (gram / 100 * a[kond][1])
        a[kond][2] == gram
        print(f"Вам надо заплатить {cost} р.")
        for key, value in a.items():
            print(f'\n{key}', f'\nОсталось {value[2]} гр.')
        print("До свидания")
        break

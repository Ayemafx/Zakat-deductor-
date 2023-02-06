print('These are the following parameters ')
parameters = ['Income', 'Gold', 'Silver', 'Property']
for i in range(len(parameters)):
    print(parameters[i])


def nisab_gold(weight):
    if weight >= 87.48:
        return 1
    else:
        print('Zakat is not  on gold')
        return 0


def nisab_silver(weight):
    if weight >= 612.36:
        return 1
    else:
        print('Zakat is not eligible on silver')
        return 0


def calculate_income():
    income = int(input('What is your amount of income or cash in hand?'))
    zakat = income * 0.025
    print(f'The zakat to be payed on your income is {zakat}')
    print('----------------------------------------------')
    return zakat


def calculate_gold():
    weight = int(input('Enter weight of gold in grams that you own'))
    if nisab_gold(weight) == 1:
        price = int(input('Enter price or value of cash of the gold you own'))
        value = weight * price
        zakat = value * 0.025
        print(f'The zakat to be payed on gold is {zakat}')
        print('----------------------------------------------')
        return zakat
    else:
        return 0


def calculate_silver():
    weight = int(input('Enter weight of silver in grams that you own'))
    if nisab_silver(weight) == 1:
        price = int(input('Enter price or value of cash of the silver you own'))
        value = weight * price
        zakat = value * 0.025
        print(f'The zakat to be payed on silver is {zakat}')
        print('----------------------------------------------')
        return zakat
    else:
        return 0


def calculate_property():
    property = int(input('Enter the current market value of the property'))
    zakat = property * 0.025
    print(f'The zakat to be payed on property is {zakat}')
    print('----------------------------------------------')
    return zakat


def calculate_total():
    total = calculate_income() + calculate_gold() + calculate_silver() + calculate_property()
    print(f'Total zakat to be payed is {total}')


calculate_total()
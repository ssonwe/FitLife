# проект FitLife - MVP версия 1.0

ML_PER_KG = 30  # стандартная рекомендация мл воды на кг веса
ML_IN_L = 1000  # мл в л

print('Добро пожаловать в FitLife — ваш уголок заботы о своем здоровье!')

# узнаем имя
while True:
    user_name = input('Подскажите, как к Вам можно обращаться? ')
    user_name = user_name.strip().title()  # удаление пробелов, заглавная буква
    if user_name:
        break
    print('Кажется, Вы не написали имя. Давайте попробуем еще раз :)')


# узнаем возраст
while True:
    try:
        user_age = int(input(f'{user_name}, сколько Вам полных лет? '))
        if user_age <= 0:
            print('Кажется, возраст указан неверно. Возраст должен быть больше'
                  ' 0. Давайте попробуем еще раз :)')
        else:
            break
    except ValueError:
        print('Пожалуйста, введите свой возраст цифрами :)')


# узнаем вес
while True:
    try:
        user_weight = float(input(f'{user_name}, какой у Вас вес(кг)? '))
        if user_weight <= 0:
            print('Кажется, вес указан неверно. Вес нужно указать в кг.'
                  ' Давайте попробуем еще раз :)')
        else:
            break
    except ValueError:
        print('Пожалуйста, введите свой вес цифрами :)')


# узнаем рост
while True:
    try:
        user_height = float(input(f'{user_name}, какой у Вас рост(м)? '))
        if user_height <= 0 or user_height >= 3:
            print('Кажется, рост указан неверно. Укажите, пожалуйста, в метрах'
                  ' (например, 1.75). Попробуем еще раз :)')
        else:
            break
    except ValueError:
        print('Пожалуйста, введите свой рост цифрами и через точку '
              '(например, 1.75). Попробуем еще раз :)')


# flake8 выдал замечания, спросила у ии как делать docstring
def calculate_bmi(weight, height):
    """расчет индекса массы тела"""
    return round(weight / (height ** 2), 1)


# здесь также flake8 выдал замечания насчет docstring, ии помог
def calculate_water(weight):
    """расчет суточной нормы воды"""
    ml_needed = ML_PER_KG * weight
    l_needed = ml_needed / ML_IN_L
    return round(l_needed, 1)


def get_bmi_info(bmi):
    """получение инфы по ИМТ"""
    if bmi < 16:
        return 'Выраженный дефицит массы тела. Необходима консультация врача!'
    elif 16 <= bmi <= 18.4:
        return 'Недостаточная масса тела. Стоит обратить внимание!'
    elif 18.5 <= bmi <= 24.9:
        return 'Масса тела в пределах здорового диапазона. Отличный результат!'
    elif 25 <= bmi <= 29.9:
        return 'Избыточная масса тела. Стоит обратить внимание!'
    elif 30 <= bmi <= 34.9:
        return 'Ожирение I степени. Необходима консультация врача!'
    elif 35 <= bmi <= 39.9:
        return 'Ожирение II степени. Необходима консультация врача!'
    else:
        return 'Ожирение III степени. Необходима консультация врача!'


water_needed = calculate_water(user_weight)
bmi = calculate_bmi(user_weight, user_height)
bmi_info = get_bmi_info(bmi)

print(f'{user_name}, спасибо за ответы!')
print(f'Вы указали возраст {user_age} лет, вес {user_weight} кг, '
      f'рост {user_height} м.')
print('На основе этих данных получилось высчитать Ваш Индекс Массы Тела, '
      'а также рекомендации по суточной норме воды.')
print(f'ИМТ составляет {bmi}.', bmi_info)
print(f'Рекомендуем пить {water_needed} л воды в день.')
print('Спасибо, что воспользовались FitLife!')
print(f'Хорошего дня, {user_name}!')

"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def print_user_data(name, surname, birth_year, residence_city, email, phone):
    """
    Output user info in one line.
    :param name: User's name.
    :param surname: User's surname.
    :param birth_year: User's year of birth.
    :param residence_city: User's city of residence.
    :param email: User's email.
    :param phone: User's phone.
    :return: None
    """
    print(f"User: {name} {surname}, year of birth: {birth_year},"
          f" city of residence: {residence_city}, email: {email}, phone: {phone}")


print_user_data(name="Anton", surname='Krivolapov', birth_year=1971, residence_city='St.Pete',
                email='akrivola@ya.ru', phone='+79999999999')

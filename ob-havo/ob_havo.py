from weather.ob_havo import Obhavo
def malumot(shaxar):
    data = Obhavo(city=f'{shaxar}').main()

    try:
        # print(data)
        city = data.get('city')
        day = data.get('day')
        info = data.get('info')
        description = data.get('description')
        degree = data.get('degree')

        text = f"""
        {day} {city} {info} {description} {degree}
        """
        return text
    except:
        return 'Malumot topilmadi'
    


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
but = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
m1 = KeyboardButton(text='Toshkent')
m2 = KeyboardButton(text='Samarqand')
m3 = KeyboardButton(text="Andijon")
m4 = KeyboardButton(text="Buxoro")
m5 = KeyboardButton(text="Jizzax")
m6 = KeyboardButton(text="Qarshi")
m7 = KeyboardButton(text="Navoi")
m8 = KeyboardButton(text="Namangan")
m9 = KeyboardButton(text="Nukus")
m10 = KeyboardButton(text="Termiz")
m11 = KeyboardButton(text="Urganch")
m12 = KeyboardButton(text="Fargona")
m13 = KeyboardButton(text="Xiva")

but.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13)

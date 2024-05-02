from PIL import Image, ImageDraw, ImageFont
def prazd():
    image_path = '../pug.hbd.jpg'
    image = Image.open(image_path)
    image.show()
    left = 10
    top = 10
    right = 500
    bottom = 500

    cropped_image = image.crop((left, top, right, bottom))

    new_image_path = 'pug.hbd2.jpg'
    cropped_image.save(new_image_path)
    print(f"Обрезанное изображение сохранено как {new_image_path}")
def prazds():
    prazd = {
        'День святого валентина': 'val.pug.jpg',
        'День рождения': 'pug.hbd.jpg',
        'Рождество': 'chrism.pug.jpg'
    }
    s = input("Напишите выбранный праздник: ")
    if s == "День святого валентина":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "День рождения":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "Рождество":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    else:
        print("Введенное значение не найдено в списке.")
def w():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя: ")
    try:
        image = Image.open("../pug.hbd.jpg")
    except IOError:
        print("Ошибка открытия изображения.")
        return

    draw = ImageDraw.Draw(image)

    text = f"{name}, поздравляю!"
    font = ImageFont.truetype('arial.ttf', 20)
    position = ((image.width) // 2, 10)  # Позиция текста в центре вверху
    draw.text(position, text, font=font, fill=(0, 0, 0))  # Исправлено на кортеж RGB
    image.save("new_pug.hbd.png")  # Исправлено: не указываем расширение

while True:
    print('1. обрезка')
    print('2. выбор')
    print('3. знак')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        prazd()
    elif a == 2:
        prazds()
    elif a == 3:
        w()
    elif a == 4:
        break
    else:
        print('Неверное действие')
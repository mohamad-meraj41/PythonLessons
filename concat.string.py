# درس سوم اتصال دو رشته ی متغیر به هم و افزودن کاراکتر از نوع رشته به متغیری که بصورت رشته تعریف شده

# متغیرهای مانند زیر تعریف کنید

name = 'Ali'
age = 34
height = 1.80
isMan = True



# در پایتون متدی است که توسط آن میتوان درون پیغام ها که بصورت استرینگ است مقادیر متغیر ها را جایگزاری کرد 
# f""
# اف استرینگ

print(f'My name is: {name}, My Age is: {age} year, My Height is: {height} cm, I am a man: {isMan}')

# در کد زیر همانطور که میبینید با استفاده از + میتوان به طول یک متغیر از نوع استرینگ اضافه کرد

lenVariable = "Categorie"
lenVariable = lenVariable + 's'  # مقدار جدید را به متغیر قبلی اختصاص می‌دهیم

print(lenVariable)  # خروجی: Categories

# یک مثال دیگر از اضافه کردن رشته به طول یک متغیر از نوع رشته

fruit = 'Apple'
fruit = fruit + 's'
print(fruit)
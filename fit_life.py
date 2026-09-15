# Константы для расчёта нормы воды
WATER_PER_KG = 30  # мл воды на 1 кг веса
ML_IN_LITER = 1000  # мл в одном литре

print("Добро пожаловать в FitLife")

# Имя пользователя
user_name = input("Введите ваше имя: ")

# Информация пользователя
try:
    user_age = int(input("Введите ваш возраст: "))
    user_weight = float(input("Введите ваш вес в кг: "))
    user_height = float(input("Введите ваш рост в метрах (например, 1.75): "))
except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")
    exit()

# Расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Расчёт суточной нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER

# Вывод результатов
print(f"Отчёт для пользователя: {user_name}, {user_age} лет")
print(f"Ваш индекс массы тела (ИМТ): {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчёт окончен. Будьте здоровы!")

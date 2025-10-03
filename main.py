import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления трапециевидной функции принадлежности
def trapezoid(x, a, b, c, d):
    """
    a, d – точки, где принадлежность равна 0
    b, c – точки, где принадлежность равна 1
    """
    # Левые и правые склоны (с защитой от деления на ноль)
    left = 0 if b == a else (x - a) / (b - a)
    right = 0 if d == c else (d - x) / (d - c)

    return np.maximum(0, np.minimum(left, np.minimum(1, right)))

# Определение нечетких множеств для температуры тела
temperature_sets = {
    "низкая":    (34, 35, 36, 36.5),
    "нормальная": (36, 36.5, 37, 37.5),
    "высокая":   (37, 38, 39, 40),
    "критическая": (39, 40, 42, 43)
}


# Определение нечетких множеств для уровня боли
pain_sets = {
    "нет боли":   (0, 0, 1, 2),
    "легкая":     (1, 2, 3, 4),
    "средняя":    (3, 4, 6, 7),
    "сильная":    (6, 7, 9, 10)
}

# === Визуализация множеств ===
x_temp = np.linspace(34, 43, 500)
x_pain = np.linspace(0, 10, 500)

plt.figure(figsize=(12, 5))

# Температура тела
plt.subplot(1, 2, 1)
for label, (a, b, c, d) in temperature_sets.items():
    plt.plot(x_temp, trapezoid(x_temp, a, b, c, d), label=label)
plt.title("Нечеткие множества: Температура тела")
plt.xlabel("Температура (°C)")
plt.ylabel("Принадлежность")
plt.legend()

# Уровень боли
plt.subplot(1, 2, 2)
for label, (a, b, c, d) in pain_sets.items():
    plt.plot(x_pain, trapezoid(x_pain, a, b, c, d), label=label)
plt.title("Нечеткие множества: Уровень боли")
plt.xlabel("Боль (0-10)")
plt.ylabel("Принадлежность")
plt.legend()

plt.tight_layout()
plt.show()

# === Ввод пользователя ===
temp_value = float(input("Введите температуру тела (°C): "))
pain_value = float(input("Введите уровень боли (0-10): "))

print("\n--- Результаты диагностики ---")

# Температура
for label, (a, b, c, d) in temperature_sets.items():
    mu = trapezoid(temp_value, a, b, c, d)
    if mu > 0:
        print(f"Температура '{label}': степень принадлежности = {mu:.2f}")

# Боль
for label, (a, b, c, d) in pain_sets.items():
    mu = trapezoid(pain_value, a, b, c, d)
    if mu > 0:
        print(f"Боль '{label}': степень принадлежности = {mu:.2f}")



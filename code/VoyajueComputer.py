# Путевой компьютер

program = "Путевой компьютер, v.0.0.1"

# Variables

stars = 80
tabs = 5

dist = 0
speed = 0
time = 0
total_time = 0
drive_hours = 0
drive_mins = 0
total_hours = 0
total_mins = 0

tank = 0
consum = 0
refuels = 0
refuel_time = 15
fuel = 0
price = 0

breaks = 0
break_time = 0

# Enter the title
print("\t"*tabs, program)
print("*"*stars)

# User inputs
dist = int(input("Введите расстояние в километрах: "))
speed = int(input("Средняя планируемая скорость: "))
consum = float(input("Введите средний расход л/100км: "))
tank = float(input("Объём бака: "))
price = float(input("Стоимость листра топлива: "))
breaks = float(input("Количество плановых остановок (без дозаправок):"))
break_time = float(input("Время каждой плановой остановки, мин: "))

# Вылисления
time = dist*60/speed
fuel = consum*dist/100 # Всего затрачено топлива
refuels = fuel // tank
total_time = time + refuels*refuel_time + breaks*break_time

drive_hours = time//60
drive_mins = time - drive_hours*60

total_hours = total_time // 60
total_mins = total_time - total_hours*60

print("*"*stars)
print("\t"*tabs, "Результаты: ")

print("Время за рулём, ч :", int(drive_hours), "ч. ", int(drive_mins), "min")
print("Общее времся в пути ч: ", int(total_hours), "ч. ", int(total_mins), "min")
print("Количество дозаправок: ", refuels)
print("Потрачено время на дозаправку: ", refuels*refuel_time, " минут")
print("Топлива потрачено: ", fuel)
print("Стоимость топлива_gfeg: ", fuel*price)
print("Hello, Hikari")

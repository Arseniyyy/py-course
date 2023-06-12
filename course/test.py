print("Добро пожаловать в Волшебный магазин доставки!")
item_name = input("Введите название волшебного предмета: ")
weight = float(input("Введите вес предмета (кг): "))
distance = float(input("Введите расстояние доставки (км): "))

if weight < 10 and distance < 100:
    delivery_cost = 200
elif weight >= 10 and weight < 50 and distance < 100:
    delivery_cost = 500
else:
    delivery_cost = 200 + 5 * distance

print(f"Стоимость доставки волшебного предмета \"{item_name}\" составляет {delivery_cost} магических монет.")


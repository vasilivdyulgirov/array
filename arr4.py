# Въвеждане на брой ученици
n = int(input("Въведи брой ученици: "))

# Въвеждане на успехите
arr = []
for i in range(n):
    grade = float(input(f"Успех на ученик {i + 1}: "))
    arr.append(grade)

# Въвеждане на търсения успех
x = float(input("Въведи успеха, който търсиш: "))

# Търсене
found = False
for grade in arr:
    if grade == x:
        found = True
        break

# Извеждане на резултата
if found:
    print("Намерен е ученик с този успех.")
else:
    print("Няма ученик с този успех.")

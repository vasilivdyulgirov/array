# Създаваме празен списък (масив)
arr = []

# Въвеждане на 5 елемента
for i in range(5):
    value = int(input(f"arr[{i}] = "))
    arr.append(value)

# Извеждане на масива
print("Въведеният масив е:")
for i in range(5):
    print(f"arr[{i}] = {arr[i]}")

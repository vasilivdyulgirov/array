# Създаваме празен списък
arr = []

# Въвеждане на 10 елемента
for i in range(10):
    value = int(input(f"arr[{i}] = "))
    arr.append(value)

# Сумиране на елементите
sum_arr = 0
for num in arr:
    sum_arr += num

# Извеждане на сумата
print(f"Сумата на елементите е: {sum_arr}")

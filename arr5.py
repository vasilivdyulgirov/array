# Даден масив
arr = [20, 8, 32, 6, 1]
n = len(arr)

# Сортиране със Selection Sort
for i in range(n - 1):
    k = i
    min_value = arr[i]
    for j in range(i + 1, n):
        if arr[j] < min_value:
            min_value = arr[j]
            k = j
    # Размяна
    arr[i], arr[k] = arr[k], arr[i]

# Извеждане на сортирания масив
for idx, value in enumerate(arr):
    print(f"arr[{idx}] = {value}")

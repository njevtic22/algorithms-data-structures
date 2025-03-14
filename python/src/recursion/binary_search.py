from src.util.arrays import generate_sorted_array


def search(data, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    mid_value = data[mid]
    if target == mid_value:
        return mid
    elif target > mid_value:
        return search(data, target, mid + 1, high)
    else:
        return search(data, target, low, mid - 1)


def main():
    data = generate_sorted_array(50)
    print("Generated array:", data)

    target = int(input("Enter number to search in array: "))
    index = search(data, target, 0, len(data))
    print("Index of searched number is:", index)

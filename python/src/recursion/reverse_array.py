from src.util.arrays import generate_sorted_array


def reverse_array(arr, low, high):
    if low >= high:
        return

    arr[low], arr[high] = arr[high], arr[low]
    reverse_array(arr, low + 1, high - 1)


def reverse_array_iterative(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def main():
    arr = generate_sorted_array(10)
    print("Normal  ", arr)

    reverse_array(arr, 0, len(arr) - 1)
    print("reversed", arr)

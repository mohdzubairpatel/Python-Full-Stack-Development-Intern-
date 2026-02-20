def print_reverse(arr, n):
    if n == 0:
        return
    print(arr[n - 1], end=" ")
    print_reverse(arr, n - 1)


arr = list(map(int, input("Enter numbers: ").split()))
print_reverse(arr, len(arr))

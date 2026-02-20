numbers = [10, 20, 30, 40]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) //StopIteration error if we try to eccess element even their is no element
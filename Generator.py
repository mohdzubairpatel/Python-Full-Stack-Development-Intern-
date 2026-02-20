def my_generator():
    yield 20
    yield 30
    yield 40
    yield 50


gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)
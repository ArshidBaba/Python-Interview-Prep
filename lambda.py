def int_multiply(x):
    return lambda c: c * x


int_double = int_multiply(2)

print(int_double(100))


nums = [1, 2, 3, 4, 5, 6]

incremented_nums = list(filter(lambda num: num % 2 != 0, nums))

print(incremented_nums)


names = ["Adam", "Kevin", "Joe"]
nums = [1, 2, 1]

mapped_names = list(map(lambda name, num: name.upper() * num, names, nums))

print(mapped_names)

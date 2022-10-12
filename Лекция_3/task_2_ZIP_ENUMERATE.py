users = ['us1', 'us2', 'us3', 'us4', 'us5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

data = list(enumerate(users))
print(data)
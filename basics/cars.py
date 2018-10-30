cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(len(cars))

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

food_list = []
food = None
while food != 'quit':
    food = input('Enter a favourite food (or \'quit\' to exit): ')
    if food != 'quit':
        food_list.append(food)

print('\nYour favourite foods are:')
for f in food_list:
    print(f)
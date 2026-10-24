# Part 1:
basket1 = {'apple','mango','apple','banana','grape'}
basket2 = {'kiwi','mango','apple','kiwi'}
print(F'Basket 1: {basket1}')
print(f'Basket 2: {basket2}')

# Part 2: Adding a new fruit to the basket
basket1.add('orange')
print('Basket 1 after adding orange -- ',basket1)

# Part 3:
common_fruits = basket1.intersection(basket2)
print('Fruits in both baskets: ',common_fruits)

# Part 4:
import array as arr
fruit_count = arr.array('i',[3,5,6,7])
print('Fuits count array: ',fruit_count)

# Part 5:
fruit_count.insert(0,1)
fruit_count.append(6)
print('Fruit count after adding items -- ',fruit_count)

# Part 6:
count_4 = fruit_count.count(4)
print('Number of 4 appeared -- ',count_4)

# Part 7:
fruit_count.reverse()
print('Fruit count after reversing -- ',fruit_count)

# Part 8: Summary
print('')
print(' ====== CLASS FRUIT BASKET ORGANIZER ======')
print(f'Basket 1          : {basket1}')
print(f'Basket 2          : {basket2}')
print(f'Shared Fruits     : {common_fruits}')
print(f'Fruit counts      : {fruit_count}')
print(' ========================================== ')
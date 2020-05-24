from datetime import date
import pet


p = pet.pet('Shadow', 'mammal', 'cat', birthdate='2019-01-01', last_fed='2020-05-19')


print(p.name, 'is', p.age(), 'years old.')
print('Today is: ' + str(date.today()))
print('Last fed: ' + p.last_fed)
print('I fed the cat today? ', p.is_fed())
print('Pet is alive?', p.is_alive())

p.feed(date.today())
print('Last fed: ' + p.last_fed)
print('I fed the cat today? ', p.is_fed())
print('Pet is alive?', p.is_alive())

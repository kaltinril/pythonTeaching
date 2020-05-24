from datetime import date, timedelta
import pet

pets = []

p1 = pet.pet('Shadow', 'mammal', 'cat')
pets.append(p1)
p1 = pet.pet('Midnight', 'mammal', 'cat', '2001-01-19', ['black'], True, False, 4, str(date.today()))
pets.append(p1)
p1 = pet.pet('Pepper', 'mammal', 'cat', last_fed=str(date.today() - timedelta(1)))
pets.append(p1)
p1 = pet.pet('Tigger', 'mammal', 'cat', last_fed=str(date.today() - timedelta(10)))
pets.append(p1)

for p in pets:
    if p.is_fed():
        print('Pet', p.name, 'is fed!')
    else:
        print('Pet', p.name, 'is not fed!')
        last_fed = p.days_since_last_fed()
        if last_fed <= 3:
            p.feed(date.today())
            print('Pet', p.name, 'was last fed', last_fed, 'days ago, and has been fed today.')
        else:
            p.died(date.today())
            print('Pet', p.name, 'died! It was last fed', last_fed, 'days ago, you monster!')



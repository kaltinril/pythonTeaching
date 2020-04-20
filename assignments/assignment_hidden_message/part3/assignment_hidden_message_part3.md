# Hidden Message Part 3

In this assignment you will copy [part1](https://github.com/kaltinril/pythonTeaching/blob/master/assignments/assignment_hidden_message/part1/assignment_hidden_message_part1.txt) to create a new part3 with your own mapping/translation functions and learn about dictionaries.

A dictionary is essentially just a `key:value` pair list, similar to **JSON**.


## Items Learned:
1. Dictionaries
1. A third way to do something to solidify concepts.

## Assignment:
1. Take part 1 and with using dictionaries, do your own mapping translation

## Requirements:
1. Must use a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp)!
1. Must not use any of these: (maketrans, translate)
1. Message should be "**_encrypted_**" and "**_decrypted_**" without errors.

---

## Lessons on Dictionaries:
### How to create a dictionary called "city_to_state"
```python
city_to_state = {'Anchorage':'Alaska','Seattle','Washington','San Fransisco':'California'}
```

### How to access an entry in the dictionary
```python
state = city_to_state['Anchorage']
print(state) # Alaska
```

### Add an item to a dictionary after creation
```python
city_to_state['Concord'] = 'New Hampshire'
```

### Remove an item from a dictionary
```python
result = city_to_state.pop('Anchorage')
```

### Getting the length of the dictionary
```python
num_of_entries = len(city_to_state)
print(num_of_entries)
```

## TIPS:
 1. Play around with dictionaries
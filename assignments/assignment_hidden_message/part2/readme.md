# Hidden Message Part 2

In this assignment you will take part 1 and adapt it to use two neat built-in string functions, (maketrans and translate)


## Items Learned:
1. Using all available python tools
1. Learning about maketrans and translate
1. Learning about creating a mapping

## Assignment:
 1. Remove the if statements and replace them with maketrans and translate.

 2. Make sure you are still reversing the message.


## Requirements:
 1. Must use maketrans and translate (appropriately)

 2. Must work for all standard first 128 ASCII printable characters.

 3. Message should be "encrypted" and "decrypted" without errors.
 
---

# How does translate and maketrans work?

`maketrans` - This creates a table of key-value pairs think of them like entangled or values that are tied together.

`translate` - This replace characters from a maketrans mapping


## Example 1
> Replace 1 with a (But does not replace a with 1)

> Replace 2 with b (But does not replace b with 2)

> Replace 3 with c (But does not replace c with 3)

```python
invalues = '123'
outvalues = 'abc'
mapping = str.maketrans(invalues, outvalues)
string_example = '123, it's easy as abc.'
string_trans = string_example.translate(mapping)
print(string_trans)
```
> abc, it's easy as abc.


## Example 2:
> Replace 1 with a, replaces a with 1

> Replace 2 with b, replaces a with 2

> Replace 3 with c, replaces a with 3

```python
invalues = '123abc'
outvalues = 'abc123'
mapping = str.maketrans(invalues, outvalues)
string_example = '123, it's easy as abc.'
string_trans = string_example.translate(mapping)
print(string_trans)
```
> abc, it's easy as 123.

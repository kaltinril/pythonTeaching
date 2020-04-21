# Hidden Message Part 1
In this assignment you will create a program that can **encrypt** or **decrypt** a message for the user.

## Items Learned:
1. String breakdown into individual characters
1. For each loops
1. Weak Encryption (obfuscation) ideas


## Assignment:
1. Ask the user for a message to encrypt or decrypt.
1. Pick at least 12 pairs of ASCII characters (letters, numbers, punctuation) to exchange values.
     - Meaning, lets say I pick these six values: A, 4, E, 3, T, 7
     - We want to convert any A's we see into 4's
     - We want to convert any 4's we see into A's
     - We want to convert any E's we see into 3's
     - We want to convert any 3's we see into E's
     - We want to convert any T's we see into 7's
     - We want to convert any 7's we see into T's

1. Reverse the entire string after conversion so it's backwards. (Helps make the message less readable)
    - Example: "I went to the park and walked my dog."
    - Result:  ".god ym d3kl4w dn4 kr4p 3h7 o7 7n3w I"
1. Test your program by running it to ENCRYPT the data.
1. Test your program by running the output from step 4 (the encrypted message) again, you should get your original message now.

## Requirements:
1. Must use a FOR EACH loop to iterate over the characters in the message
     - Example: Loop over the items in a list
     ```python
     conversion_temperatures = ['C', 'F', 'K']
     for type in conversion_temperatures:
        print(type)
     ```
     - Example: Loop over the letters in a string
     ```python
     name = 'Kaltinril'
     for letter in name:
        print(letter)
     ```
1. Must work for all standard first 128 ASCII printable characters.
1. Message should be "encrypted" and "decrypted" without errors.


## Getting Started:
1. Get the message from the user
1. Loop over the message, checking each letter to see if you need to change it into a different letter
1. Reverse the string
1. print out the result


## TIPS:
1. Get this working without the reverse first to make sure the conversions are working.

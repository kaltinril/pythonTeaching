# Get user input, and store in variable called "Message"
message = input("What is your message? ")
secret = ""

mapping = {
    'a':'4', '4':'a',
    'e':'6', '6':'e',
    'i':'1', '1':'i',
    'o':'0', '0':'o',
    'u':'7', '7':'u',
    'y':'5', '5':'y'  
}

# Loop over each letter in the message, converting it to it's partner character
# Each partner character is hard coded for this simple example
for letter in message:
    if letter in mapping:
        letter = mapping[letter]
    else:
        letter = letter

    # Reverse the message (using logic) [Option 1]
    # This essentially builds the secret backwards, 
    # which has the effect of reversing the string
    secret = letter + secret

print(secret)

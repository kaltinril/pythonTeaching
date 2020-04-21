# Get user input, and store in variable called "Message"
message = input("What is your message? ")
secret = ""

# Loop over each letter in the message, converting it to it's partner character
# Each partner character is hard coded for this simple example
for letter in message:
    if letter == "a": letter = "4"
    elif letter == "e": letter = "6"
    elif letter == "i": letter = "1"
    elif letter == "o": letter = "0"
    elif letter == "u": letter = "7"
    elif letter == "y": letter = "5"
    elif letter == "4": letter = "a"
    elif letter == "6": letter = "e"
    elif letter == "1": letter = "i"
    elif letter == "0": letter = "o"
    elif letter == "7": letter = "u"
    elif letter == "5": letter = "y"
    else:
        letter = letter

    # Reverse the message (using logic) [Option 1]
    # This essentially builds the secret backwards, 
    # which has the effect of reversing the string
    secret = letter + secret
    

# Reverse the message (Using Slice) [Option 2]
#secret = secret[::-1]

# Reverse the message (Using reversed and join) [Option 3]
# secret = "".join(reversed(string)) 

# Reverse the message (Using a loop) [Option 4]
# I've decided that there isn't much of a point to code this one

print(secret)

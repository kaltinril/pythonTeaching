# Get user input, and store in variable called "Message"
message = input("What is your message? ")

# Build input and output value mappings
invalues = 'aeiouy461075'
outvalues = '461075aeiouy'
mapping = str.maketrans(invalues, outvalues)

# Do the replaces
secret = message.translate(mapping)

# Reverse the string
secret = secret[::-1]

print(secret)

# Fortune teller
print("I will predict who I am speaking to by asking these questions.")
print("")

# Ask 6 questions and store the answers (converted to upper-case)
color = input("What is your favorite color? ").upper()          # purple
pets = input("How many pets do you have? ").upper()             # 3
candy = input("What is your favorite candy? ").upper()          # Skittles
hs = input("What was your high school? ").upper()               # Dimond
book = input("What is one of your favorite books? ").upper()    # City of Ember
sport = input("Name one of your favorite sports. ").upper()     # volleyball, softball

# Calculate how many match our knowledge of Miss Alward
correct = 0
if color == "PURPLE":
  correct = correct + 1
if pets == "3":
  correct = correct + 1
if candy == "SKITTLES":
  correct = correct + 1
if hs == "DIMOND" or hs == "DIMOND HIGH" or hs == "DIMOND HIGH SCHOOL":
  correct = correct + 1
if book == "CITY OF EMBER":
  correct = correct + 1
if sport == "VOLLEYBALL" or sport == "SOFTBALL":
 correct = correct + 1

# Check if 4, 5, or 6 of the answers matched out knowledge of Miss Alward
if correct > 3:
  print("We think you are the Awesome Miss Alward! ")
else:
  print("We were hoping you'd be Awesome Miss Alward??")
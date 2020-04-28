keep_running = 'Y'
while keep_running == 'Y':
  sides = input("How many sides does your shape have? ")
  
  p = 0
  for side in range(0, int(sides)):
    s = input("Enter length of side " + str(side+1))
    p = p + int(s)
  
  print("The perimeter of your " + str(sides) + " shape is " + str(p))

  keep_running = input("Calculate another shape? [Y/N] ").upper()

#Asking the user about the desired type of adventure
print("What kind of adventure are you looking for?")
#Defining the types of adventures
adventure=input()
if((adventure=="short") or (adventure=="scary")):
  print("Entering in the dark forest!")
elif((adventure=="safe") or (adventure=="long")):
  print("Taking the safe route!")
else:
  print("Not sure which route to take!")






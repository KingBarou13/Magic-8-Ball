while True:
  print("Welcome To The Magic 8 Ball.\n")
  input("State your question and I shall provide my wisdom: ")
  
  import random
  import time
  
  print("\nThinking...\n")
  time.sleep(5)
  
  responsesPos = ["It is certain", "It is decidedly so", "Without a doubt", "Absolutely", "Yes", "Probably", "You can count on it"]
  
  responsesUncertain = ["It is best not to answer that", "Unable to make such a prediction", "Try again later"]
  
  responsesNeg = ["No", "That is highly unlikely", "Don't count on it", "I am very doubtful"]
  
  pick1 = random.choice(responsesNeg)
  pick2 = random.choice(responsesUncertain)
  pick3 = random.choice(responsesPos)
  Magic = [pick1 ,pick2,pick3]
  
  print(random.choice(Magic))

  while True:
      answer = input('\nDo you have any further questions? (y/n): ')
      if answer in ('y', 'n'):
          break
      print("\nI do not understand... \n\n Please Try Again.")
  if answer == 'y':
      continue
  else:
      print("\nFarewell...")
      break
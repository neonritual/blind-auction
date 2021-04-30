from replit import clear
#HINT: You can call clear() to clear the output in the console.

x = True
bid_dictionary = {}
top_score = 0
while x is True:
  name = input("What's your name?\n")
  bid = input("What's your bid?\n")
  bid_dictionary[name] = bid
  print(bid_dictionary)
  more_players = input("Are there any other players?\n")
  if more_players == "no":
    clear()
    x = False
    maximum = max(bid_dictionary, key=bid_dictionary.get)  # Just use 'min' instead of 'max' for minimum.
    print(f"The top bidder is {maximum}, with a big of ${bid_dictionary[maximum]})
  else: 
    clear()
    continue

    

# take_bids()
# bid_dictionary[name] = bid

# print(bid_dictionary)
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

x = True
bid_dictionary = {}
top_score = 0
while x is True:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n$"))
    bid_dictionary[name] = bid
    print(bid_dictionary)
    more_players = input("Are there any other players?\n")
    if more_players == "no":
        clear()
        x = False
        for player in bid_dictionary:
          bid_amount = bid_dictionary[player]
          if bid_amount > top_score:
            top_score = bid_amount
            winner = player
        print("The winning bid is " + str(winner) + " with $" + str(top_score) + ". Congrats!")
        
    else:
        clear()
        continue

#From here is the teacher's solution, for comparison and study purposes笑

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   #bidding_record = ("Angela": 123, "James": 321)
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
  
# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[names] = price
#   should_continue = input ("Are there any other bidders? Type 'yes' or 'no'.")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()

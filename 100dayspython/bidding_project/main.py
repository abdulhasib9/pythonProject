from art import logo
print(logo)



def findhighest_bidder(bidding_record):
    highest_bid =0
    winner =""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner=bidder
    print(f"the winner is  {winner} with highest bid of ${highest_bid}")




bids ={}
bidding_finished =False
while not bidding_finished:
    name= input("what is your name?")
    price =int(input("what is your bid ? $"))
    bids[name]=price
    should_continue=input("are ther any other bidders? Type 'Yes or No' ")
    if should_continue.lower() == 'no':
        bidding_finished=True
        findhighest_bidder(bids)
        

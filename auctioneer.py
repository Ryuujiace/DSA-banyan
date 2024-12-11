from banyan import SortedDict  # Use SortedDict to store bids

class Auctioneer:
    def __init__(self, starting_item, starting_price):
        self.current_item = starting_item
        self.current_price = starting_price
        self.highest_bidder = None
        self.bids = SortedDict()  # Initialize SortedDict to store bids

    def start_auction(self):
        print(f"Auction started for {self.current_item} with a starting price of ${self.current_price}.")

    def receive_bid(self, bidder, amount):
        # Ensure the bid is at least 5 higher than the current price
        if amount >= self.current_price + 5:
            self.current_price = amount
            self.highest_bidder = bidder
            self.bids[bidder] = amount  # Store the bid in SortedDict
            return True
        return False

    def announce_winner(self):
        if self.highest_bidder:
            print(f"Auction ended! Winner: {self.highest_bidder} with a bid of ${self.current_price}.")
            # Show all bids in sorted order
            print("All bids placed:")
            for bidder, bid in self.bids.items():
                print(f"{bidder}: ${bid}")
        else:
            print("Auction ended with no valid bids.")

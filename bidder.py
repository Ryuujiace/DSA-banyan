# bidder.py
class Bidder:
    def __init__(self, name):
        self.name = name

    def place_bid(self, auctioneer, amount):
        success = auctioneer.receive_bid(self.name, amount)
        if success:
            print(f"{self.name} placed a bid of ${amount}.")
        else:
            print(f"{self.name}'s bid of ${amount} was rejected.")

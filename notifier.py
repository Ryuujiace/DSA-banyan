# notifier.py
class Notifier:
    def broadcast(self, current_price, highest_bidder):
        print(f"Current highest bid: ${current_price} by {highest_bidder}")

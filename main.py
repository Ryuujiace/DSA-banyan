from auctioneer import Auctioneer
from bidder import Bidder
from notifier import Notifier
from logger import Logger

def main():
    # Initialize components
    auctioneer = Auctioneer("Antique Vase", 100)  # Auction for "Antique Vase" starting at $100
    notifier = Notifier()  # Notifier to broadcast the auction updates
    logger = Logger()  # Logger to log auction events

    # Initialize bidders
    bidders = [Bidder("Alice"), Bidder("Bob"), Bidder("Charlie")]

    # Start auction
    logger.log_event("Auction started.")
    auctioneer.start_auction()

    # Simulate bidding
    bids = [(bidders[0], 105), (bidders[1], 110), (bidders[2], 115), (bidders[0], 120)]
    for bidder, bid in bids:
        if auctioneer.receive_bid(bidder.name, bid):  # Bidder places a bid
            notifier.broadcast(auctioneer.current_price, auctioneer.highest_bidder)  # Notify about the new highest bid
            logger.log_event(f"Bid: {bidder.name} placed ${bid}.")  # Log the bid
        else:
            logger.log_event(f"Invalid bid: {bidder.name} attempted ${bid}.")  # Log invalid bid

    # End auction
    auctioneer.announce_winner()  # Announce the winner of the auction
    logger.log_event("Auction ended.")  # Log the end of the auction

if __name__ == "__main__":
    main()  # Run the main function when the script is executed

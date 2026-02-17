# print("hello")
# print("\n" * 50)
# input("Type: ")

print("Welcome to the bidding world")
others_bidders = True
encheres = {}
highest_bidder = 0
while others_bidders:
    Name = input("Whats your name : ")
    Bid = int(input("Whats your Bid : $ " ))
    encheres = {Name: Bid}
    encheres[Name] = Bid

    bidders_2 = input("Are they others bidders ? Type : yes or no :  ").lower()
    print("\n" * 50)

    if bidders_2 == "no":
        others_bidders = False
for i in encheres:
    mise = encheres[i]
    if mise > highest_bidder:
        highest_bidder = mise
        winner = Name
    print(f"le gagnant est : {winner} avec {highest_bidder}$")
  


import icon_of_hamar
print(icon_of_hamar.logo)
dic = {}
print("welcome to secrect ocction program!!")




def bid_calcu(dic):
    winer = ""
    bid_amount = 0
    for bidder in dic:
        if bid_amount < dic[bidder]:
            winer = bidder
            bid_amount = dic[bidder]
    print(f"{winer} win the bid his/her bid ammount {bid_amount}")


while True:

    name = input("what is your name?").lower()
    bid = int(input("what is your bid?"))
    dic[name] = bid
    bid_ye = input("are there any other bid? yes or no").lower()

    if bid_ye == "yes":
        continue
    else:
        bid_calcu(dic)
        break

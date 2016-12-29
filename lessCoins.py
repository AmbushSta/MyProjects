"""
Takes in an integer representing the amount of cents you have, and prints
the amount of notes you can acquire including fifty and ten cents.
Author: Michael Cowie
"""

def lessCoins(n_cents):
    nzCurrency = [(500, 'Five dollar note'),(200,'Two dollar coin'),(100, 'One dollar coin'),
                  (50, 'Fifty cent coin'),(10, 'Ten cent coin')]
    for value, currency in nzCurrency:
        requiredAmount = n_cents // value
        if requiredAmount > 0:
            if currency.split()[2] == "coin" and requiredAmount != 1:
                print("You will require {} {}s".format(requiredAmount, currency))
            elif currency.split()[2] == "coin" and requiredAmount == 1:
                print("You will require {} {}".format(requiredAmount, currency))
            elif currency.split()[2] == "note" and requiredAmount != 1:
                print("You will require {} {}s".format(requiredAmount, currency))
            else:
                print("You will require {} {}".format(requiredAmount, currency))                 
            n_cents = n_cents - (requiredAmount * value)
            
lessCoins(12345)
"""
Will output::
You will require 24 Five dollar notes
You will require 1 Two dollar coin
You will require 1 One dollar coin
You will require 4 Ten cent coins
"""

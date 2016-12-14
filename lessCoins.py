def lessCoins(n_cents):
    nzCurrency = [(500, 'Five dollars'),(200,'Two dollars'),(100, 'One dollar'),
                  (50, 'Fifty cents'),(10, 'Ten cents')]
    for value, currency in nzCurrency:
        requiredAmount = n_cents // value
        if requiredAmount > 0:
            print("You will require {} {} pieces".format(requiredAmount, currency))
            n_cents = n_cents - (requiredAmount * value)    //Remove cents

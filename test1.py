#Currency
GBP = 1
EUR = 2
USD = 5
JPY = 4
Currency = raw_imput("Currency you want to change from (GBP, EUR, USD, JPY?")
if Currency.isalpha:
    print "You did not input a correct Currency"
    break
Ammount = raw_input("Ammount of currency you want to convert e.g 3.75")
to = raw_imput("Currency converting to?")

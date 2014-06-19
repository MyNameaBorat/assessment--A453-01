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
if Currency = GBP and to = EUR:
    print ammount*2
if Currency = GBP and to = USD:
    print ammount*5
if Currency = GBP and to = JPY:
    print ammount*4
if Currency = GBP and to = GBP:
    print ammount*1
if Currency = USD and to = USD:
    print ammount*1
if Currency = USD and to = EUR:
    print ammount*0.40
if Currency = USD and to = JPY:
    print ammount*0.80
if Currency = EUR and to = EUR:
    print ammount*1
if Currency = EUR and to = GBP:
    print ammount*0.50
if Currency = EUR and to = JPY:
    print ammount*2
if Currency = EUR and to = USD:
    print ammount*2.50
if Currency = JPY and to = EUR:
    print ammount*0.50
if Currency = JPY and to = USD:
    print ammount*1.20
if Currency = JPY and to = GBP:
    print ammount*0.20
if Currency = JPY and to = JPY:
    print ammount*1
    
#This should make the ammount you put in total to the exchange rate of the other rates

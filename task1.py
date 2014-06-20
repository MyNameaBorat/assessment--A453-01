currs = ['GBP', 'EUR', 'USD', 'JPY']
rates = [1,1.2,1.3,1.4] # startup rates

def conv(money, cFrom, cTo):
    answer = money *rates[cTo]
    answer = answer /rates[cFrom]
    return (answer)
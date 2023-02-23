#Currency converter (Need to install forex-python using: pip install forex-python)

#import the forex_python library

from forex_python.converter import CurrencyRates

#create the curency variable
current = CurrencyRates()

#function to convert currency
def convert(amount, from_currency, to_currency):
    return current.convert(from_currency, to_currency, amount)

#Get input from the user
amount = float(input("Enter amount you want to convert: "))
print("Note: Enter currency using capital letter eg.(USD, JPY, EUR)")
from_currency = input("Enter currency to convert from: (eg. USD) ")
to_currency = input("Enter currency to convert to: eg. EUR")

result = convert(amount, from_currency, to_currency)
if result:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
else:
    print("Currency conversion failed")
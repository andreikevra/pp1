#VAT Calculator

def get_price():
    price = float(input("How much did you pay?"))
    return price

def VAT(price):
    VAT = round(.23 * price,23)
    return VAT

def final_price(price,VAT):
    final_price = price - VAT
    return final_price

def display(price, VAT):
    print ("Amount PLZ","%.2f" % price)
    print ("The VAT you payed came to PLZ","%.2f" % VAT)
    print ("Your final payment after VAT is PLZ","%.2f" % final_price)

price = get_price()
VAT = VAT(price)
final_price = final_price(price,VAT)
display(price,VAT)
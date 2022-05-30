class money:
    def __init__(self, euro):
        self.euro = euro
    def get_usd(self):
        usd = self.euro * 1.1
        return usd
    
    def get_gbp(self):
        gbp = self.euro * 0.9
        return gbp

wallet = money(euro=100)
usd = wallet.get_usd()
print(usd)
gbp = wallet.get_gbp()
print(gbp)

# class Money:
    
#     # KLASES ATRIBŪTS
#     # vienāds viesiem objektiem
#     rates = {
#         'USD': 1.08,
#         'GBP': 0.85,
#     }

#     def __init__(self, euro):
#         # INSTANCES ATRIBŪTS
#         # katram objektam savs
#         self.euro = euro

#     def usd(self):
#         return self.euro * Money.rates['USD']

#     def gbp(self):
#         return self.euro * Money.rates['GBP']


# wallet = Money(euro=215)
# print(wallet.usd())

class Price():
    def __init__(self,total_money,chocolate_price):
        self.total_money=total_money
        self.chocolate_price=chocolate_price
    def returned(self):
        returned_money=self.total_money%self.chocolate_price
        number=self.total_money//self.chocolate_price
        print('The customer can buy',number,'chocolates','\n',returned_money,'yuan will be returned')
example=Price(150,8)
Price.returned(example)
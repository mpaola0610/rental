class bigPocks:
    
    def __init__(self, cost, units, closingCost= 3000):
        self.cost = cost
        self.units = units
        self.closingCost = closingCost
        
        

        

    def income(self):
        self.income = 0
        rent = int(input(f'The charge per unit is:'))
        misc = int(input(f'Enter any other random incomes you may have: '))
        self.income += rent
        self.income += misc
    


    def payexpenses(self):
        self.expenses = 0
        taxes = 150 
        print(f'\nYour taxes are: ${taxes}')
        insurance = 150
        print(f'\nYour insurance is: ${insurance}')
        utilities = 50
        print(f'\nYour utilities are: ${utilities}')
        vacancy = 100
        print(f'\nYour vacancy: ${vacancy}')
        repairs= 100
        print(f'\nYour repairs: ${repairs}')
        capex= 100
        print(f'\nYour capex: ${capex}')
        mortgage= 0
        if self.cost <= 100000:
            mortgagae += 400
        elif self.cost > 100000 and self.cost < 500000:
            mortgage += 800
        elif self.cost >500000:
            mortgage += 1200   
        self.expenses += taxes
        self.expenses += insurance
        self.expenses += utilities
        self.expenses += vacancy
        self.expenses += repairs
        self.expenses += capex
        self.expenses += mortgage
        print(self.expenses)

        print(f'These are your total expenses: {self.expenses} ')

 


    def cashflow(self):
        self.yourcashflow = self.income - self.expenses
        print(f'We are almost done, here is your total monthly cash flow:{self.yourcashflow}')





    def roi(self):
        self.totalinvestment = 0
        rehabbudget = 7000
        downpayment = int(input(f'What did you pay for downpayment?:'))
        self.totalinvestment += rehabbudget
        self.totalinvestment += downpayment
        self.totalinvestment += self.closingCost
        print(f'Your total investment is:{self.totalinvestment}')

        annualcashflow = self.yourcashflow * 12 
        
        cashreturn = self.totalinvestment/annualcashflow
        

        

        print(f'Now that we got your total investment {self.totalinvestment} we can divide that by your annual cashflow {self.yourcashflow} to give us your cash on cash RETURN! {cashreturn}')        
        

randomHouse = bigPocks(200000, 4)

def run(house):
    house.income()
    house.payexpenses()
    house.cashflow()
    house.roi()

run(randomHouse)

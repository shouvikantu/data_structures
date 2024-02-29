class CreditPlan:
    def __init__(self, purchase_price):
        self.purchase_price = purchase_price
        self.annual_interest_rate = 0.12
        self.down_payment_rate = 0.10
        self.monthly_payment_rate = 0.05
        self.down_payment = self.calculate_down_payment()
        self.initial_balance = self.calculate_initial_balance()
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_down_payment(self):
        return self.purchase_price * self.down_payment_rate

    def calculate_initial_balance(self):
        return self.purchase_price - self.down_payment

    def calculate_monthly_payment(self):
        return self.initial_balance * self.monthly_payment_rate

    def calculate_payment_schedule(self):
        balance = self.initial_balance
        month = 0

        print(f"{'Month':>5} | {'Balance':>10} | {'Interest':>8} | {'Principal':>9} | {'Payment':>8} | {'Remaining':>10}")
        print("-" * 65)

        while balance > 0:
            month += 1
            interest = balance * (self.annual_interest_rate / 12)
            principal = min(self.monthly_payment - interest, balance)
            remaining_balance = balance - principal
            print(f"{month:>5} | {balance:>10.2f} | {interest:>8.2f} | {principal:>9.2f} | {self.monthly_payment:>8.2f} | {remaining_balance:>10.2f}")
            balance = remaining_balance

            if balance < self.monthly_payment:
                self.monthly_payment = balance + interest

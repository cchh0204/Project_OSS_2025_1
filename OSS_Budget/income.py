
class Income:
    def __init__(self, date, source, description, amount):
        self.date = date
        self.source = source
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.source} - {self.description}: +{self.amount}원"
    
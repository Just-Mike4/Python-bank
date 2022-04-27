class Bank:
	def __init__(self,name,amount):
		self.name=name
		self.amount=amount
		
	def Credit(self,add):
		self.amount += add
		print("Name:",self.name,"\nNew Amount:" ,self.amount)
		
	def Debit(self,sub):
		self.amount -= sub
		print("Name:",self.name,"\nNew Amount:" ,self.amount)
		
	def Loan(self,loan,days):
		self.amount += loan
		print("Name:",self.name,"\nNew Amount:",self.amount, "\nLoan", loan,"to be returned in",days,"days")
		
		
James=Bank("James",1000)
James.Credit(300)

John=Bank("John",1400)
John.Debit(200)

Adam=Bank("Adam",2000)
Adam.Loan(5000,30)

		
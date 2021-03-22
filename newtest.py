class Test():
	def __init__(self):
		self.a = "HELLO"
		self.b = "WORLD"

	def vote(self):
		print(f'{self.a} {self.b} !')

t = Test()
t.vote()

print('this is extremely new file available only in branch test!')
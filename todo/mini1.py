class TODO:
	def __init__(self):
		self.to_do=[]
		self.done=[]

	def add(self):
		inp=eval(input("Enter the task:"))
		self.to_do.append(inp)
	def mark_done(self):
		inp=eval(input("Enter the Task:"))
		if inp in self.to_do:
			
			#temp=inp
			self.to_do.remove(inp)
			self.done.append(inp)
		else:
			print("Task Not Present At All to Remove It from Present List! ")
	def see_tasks(self):
		print(self.to_do)
		print("In to_do List:")
		for i in self.to_do:
			print(i)
		print("In Done List:")
		for i in self.done:
			print(i)
	

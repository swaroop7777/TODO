from mini1 import TODO

c=TODO()
while True:
	print("choose one\n1.add\n2.mark done\n3.see lists\n")
	ch=eval(input("enter your choice:"))
	if ch==1:
		c.add()
	elif ch==2:
		c.mark_done()
	elif ch==3:
		c.see_tasks()
	else:
		print("select valid option!")



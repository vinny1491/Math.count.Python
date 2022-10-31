#pylint:disable= '\В'. String constant might be missing an r prefix.
#pylint:disable=E0001
#pylint:disable=E0001
print("""пк составит пример,а ты попробуй решить,для остановки напиши STOP.""")
print("-"*43)

###########################

import random 
digit1=10   #нижний диапазон
digit2=100 #высокий диапазон
sign=0        #знак + - * /
game=True #главный цикл
right=0       #верные ответы
score=0      #очки
count=0	#вып.задачи


###########################

while(game):
	print(f"Ваши очки:{score}")
	print(f"Выполнено задач:{count}")
	print(f"Правильных задач:{right}")
	print("_"*43)

	sign=random.randint(0,3)
	#0- +
	#1- -
	#2- *
	#3- /

# *******************СЛОЖЕНИЕ	
	if (sign==0):
		z=random.randint(digit1,digit2)
		x=random.randint(digit1,z)
		y=z-x
		if (random.randint(0,1)==0):
			print(f"{x}+{y}=?")
		else:
			print(f"{y}+{x}=?")
# *******************ВЫЧИТАНИЕ
	elif(sign==1):
		x=random.randint(digit1,digit2)
		y=random.randint(0,x-digit1)
		z=x-y
		print(f"{x}-{y}=?")
# ****************** УМНОЖЕНИЕ
	elif(sign==2):
		x=random.randint(1,(digit2-digit1)//
		random.randint(1,digit2//10)+1)
		y=random.randint(digit1,digit2)//2
		z=x*y
		print(f"{x}*{y}=?")
# *******************ДЕЛЕНИЕ
	elif(sign==3):
		x=random.randint(1,(digit2-digit1)//
		random.randint(1,digit2//10)+1)
		y=random.randint(digit1,digit2)//x
		if(y==0):
			y=1
		x=x*y
		z=x//y
		print(f"{x}/{y}=?")
		
###########################

	user = " "
	while(not user.isdigit()
			and user.upper() !="STOP"
			and user.upper() !="S"
			and user.upper() !="Ы"
			and user.upper() !="ЫЕЩЗ"):
		user = input ("ваш ответ:")
		
		if(user.upper()=="HELP"
					or user == "?"
					or user== ","
					or user.upper()== "РУДЗ"):
			if(z>9):
				print(f"последняя цифра ответа:{z % 10}")
			else:
				print("ответ состоит из ожной цифры.Подсказка не возможно.")
			score -= 10
			
		elif(user.upper()=="STOP"
						or user.upper()=="S"
						or user.upper()=="Ы"
						or user.upper()=="ЫЕЩЗ"):
			game=False
		else:
			count +=1
			if(int(user)==z):
				print("\nПраильно.\n")
				right+=1
				score+=10
			else:
				print(f"\nОтвет неверный...Правильный ответ {z}")
				print(f"\Вы можете ввести команду HELP или ?, чтобы увидеть последнюю цифру ответа(-10 очков)\n")
				score-=20	

#######################

print("*"*43)
print("СТАТИСТИКА ИГРЫ:")
print(f"Всего примеров:{count}")
print(f"Правильных ответов:{right}")
print(f"Не правильных ответов {count-right}")
if (count>0):
		print(f"процент правильных ответов: {int(right/count*100)}%")
else:
	print("процент верных ответов 0%")

																		
print("Возвращайтесь")																																																														
																					
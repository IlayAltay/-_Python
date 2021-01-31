#подклчить модуль 
#сгенерировать случайное число


from math import*
import random

############################################################################
def is_valid(text):
	w=[x  for x in text]
	for i in range(0,len(w)):
		if w[i].isdigit()==False: 
			return False
	s=''.join(w)
	n=int(s)
	if 1<=n<=100:
		return True
	else:
		return False
###########################################################################
def is_validgr(text):
	w=[x  for x in text]
	for i in range(0,len(w)):
		if w[i].isdigit()==False: 
			return False
	s=''.join(w)
	n=int(s)
	if 0<=n<=1000:
		return True
	else:
		return False
###########################################################################3
def starting_game():
	flag=0
	flag2=0
	flag3=0
	
	print('Добро пожаловать в числовую угадайку')
	print('Хотите задать диапазон для выбора случайноно числа?')
	print('Нажмите Y если хотите задать или N если хотите оставить по умолчанию')
	while flag==0:
		s=input()
		if s.isalpha():
			if s.lower()=='y':
				print('Введите левую границу диапазона:')
				while flag2==0:
					grl=input()
					if is_validgr(grl):
						grl=int(grl)
						flag2=1
					else:
						print('Введите ВЕРНОЕ  число для левой границы...0....n')
				print('Введите правую границу диапазона:')
				while flag3==0:
					grr=input()
					if is_validgr(grr):
						if int(grr)<=grl:
							print('Число меньше чем левая граница, введите большее число ...')
						else:
							grr=int(grr)
							flag3=1
					else:
						print('Введите ВЕРНОЕ  число для правой границы...0....n')
				print('Границы диапазона сформированы')
				print('Игра началась!')		
				return random.randint(grl,grr)		
			elif s.lower()=='n':
				flag=1
				print('Границы диапазона сформированы')
				print('Игра началась!')
				return random.randint(1,100)
			else:
				print('попроуйте ввести верный символ...')
				
###########################################################################
def current_game(num):
	flag=0
	flag2=0
	count=0
	
	while flag==0:
	
		while flag2==0:
			print('Ввeдите число:')
			x=input()
			if is_valid(x):
				flag2=1
				n=int(x)
				count+=1
			else:
				print('А может быть все-таки введем целое число от 1 до 100?')
			#flag=0
		#while flag==0:
			if flag2==1:
				if n>num:
					print('Ваше число больше загаданного, попробуйте еще разок')
					flag2=0
				elif n<num:
					print('Ваше число меньше загаданного, попробуйте еще разок')
					flag2=0
				elif n==num:
					print('Вы угадали, поздравляем!')
					flag=1
			
	print('Спасибо, что играли в числовую угадайку. Еще увидимся...')		
	print('Число попыток:',count)
#########################################################################3#
def continue_game():
	flag=0
	print('Желаете сыграть еще?', 'Y or N')
	while flag==0:
		s=input()
		if s.isalpha():
				if s.lower()=='y':
					return 1
				elif s.lower()=='n':
					return 0
				print('попроуйте ввести верный символ...')
		else:
			print('попроуйте ввести верный символ...')
###########################################################################
#num=random.randint(1,100)
#Основная программа
start_flag=1

num=starting_game()

while start_flag==1:
	current_game(num)
	start_flag=continue_game()
	

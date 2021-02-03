import random

def generate_password(w,length):
    s=''.join(random.sample(w,length))
    return s

##########################################################
digits='0123456789'
uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'

punctuation='!#$%&*+-=?@^_.'
controversial_simbol='il1Lo0O'

#chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars = ''

print('Укажите количество паролей для генерации_')
n=int(input())
print('Укажите длину пароля_')
length=int(input())
print('Включать цифры?','да/нет')
digit=input().lower()
print('Включать ли прописные буквы?','да/нет')
#print(uppercase_letters)
uppalpha=input()
print('Включать ли строчные буквы?','да/нет')
lowalpha=input()
print('Включать ли символы?','да/нет')
simbol=input()
print('Исключать ли неоднозначные символы il1Lo0O   ?','да/нет')
similar_simbol=input()

if digit=='да' or digit=='yes' or  digit=='y' :
    chars=chars+digits
print(chars)
if uppalpha=='да' or uppalpha=='yes' or  uppalpha=='y':
    chars+=uppercase_letters
    #print('сложил')
print(chars)

if simbol=='да' or simbol=='yes' or  simbol=='y':
    chars=chars+punctuation

if lowalpha=='да' or lowalpha=='yes' or  lowalpha=='y':
    chars+=lowercase_letters
    #print('сложил')
#print(chars)    
w=list(chars)
#print(chars)
#print(w)    
if similar_simbol=='да' or similar_simbol=='yes' or  similar_simbol=='y':
    for x in controversial_simbol:
        if x in w:
            w.remove(x)
print(*w,sep='_')

print('осуществляется генерация...')

for i in range(0,n):
    print(generate_password(w,length))

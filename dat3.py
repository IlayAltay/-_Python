import time
import dat1

interval=5 #sec  for write data
seconds=int()
last_time=int()
current_time=int()
current_temp=0
info_from_sensor_list=[]  #запись раз в пять мин 60 знчений
count=0   # счетчик до 60 записей в список
line=str()
len_list_temp=12 #длина списка записей температуры

last_time=time.time()
current_time=last_time

def add_file_infT(s_info):
    myfile=open("data_temp.txt",'a')
    for x in s_info:
        myfile.write(x)
    myfile.close()

while True:
    #print("Вввести 1 символ_")
    #a=input()
    #print("ВВести 2 й символ_")
    #b=input()
    #print("Результат:",a,b)
    current_time=time.time()
    
    #print("Секунды_",time.ctime(current_time))
    
    if (current_time-last_time)>interval:
        #print("Измерение")
        last_time=current_time
        current_temp=dat1.get_temp()
        line=str(current_temp)+' _'+time.ctime(current_time)+'\n'
        info_from_sensor_list.append(line)
        count+=1
        #print("Температура:",current_temp)
        #print(line)
    if count==len_list_temp:
        add_file_infT(info_from_sensor_list)
        count=0
        info_from_sensor_list.clear()

    time.sleep(1)

    #print("Выйти?")
    #c=input()
    #if c =='q':
     #   break
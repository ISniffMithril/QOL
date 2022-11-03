###Бесполезный помощник который будет помогать делать бесполезные вещи###
#### Ver 0.01 ####

#Импортирование библиотек
import os
import time
import random

#Константные переменные 
one  = 1

#if not os.path.isdir("жопа"):  #проверка отсутствия папки если нету то создаёт
#       os.mkdir("жопа")


#Текущее время
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#Импорт данных если они есть

#Метод 1 входа 
#if not os.path.isdir("Settings"):  #проверка отсутствия папки Settings
first_login = 0 #Изменить потом
if first_login == 0: #Изменить потом
    #Создание служебных папок
    #Загрузки

    ####                            ПОТОМ УБРАТЬ                                                        #####

    i=1
    if i == 0:
       #Загрузки
       os.mkdir("Downloads")
       os.makedirs("Downloads/Videos")
       os.makedirs("Downloads/Images")
       os.makedirs("Downloads/Gifs")
       os.makedirs("Downloads/Text")

       #Настройки и конфиг
       os.mkdir("Settings") 
       os.mkdir("Settings/User")
       os.mkdir("Settings/Config")
    
    


    #Создание файлов конфига
    #README ОСНОВА
    
    ####                            ПОТОМ УБРАТЬ                                                        #####
    if i == 0:
    
        README = open("README.txt", "w") # создать новый текстовый файл 
        README.write("Типичный текст README") # запить текста в этот файл #####          !!!!НАПИСАТЬ нормальный текст
        README.close()
    
        #Создание файлов конфига
        #README конфиг
        README2 = open("README_Before_Use.txt", "w") # создать новый текстовый файл 
        README2.write("Типичный текст README") # запить текста в этот файл #####         !!!!НАПИСАТЬ нормальный текст
        README2.close()
        os.replace("README_Before_Use.txt", "Settings/README_Before_Use.txt")

        #Файл Конфига
        Config = open("Config.txt", "w") # создать новый текстовый файл 
        Config.write("sdf") # запить текста в этот файл
        Config.close()
        os.replace("Config.txt", "Settings/Config/Config.txt")
        
    
    #Сбо информации о пользователе
    print("Добро пожаловать в бесполезную программу. Как вас зовут?")
    name_user = input("Введите ваше имя:")

    #Запись всех данных в конфиг и из сохрание

#INFINYTY LOOP
if one == 1:

    if first_login == 1:
        print("Добро пожаловать", name_user, "Чем могу помочь?" )

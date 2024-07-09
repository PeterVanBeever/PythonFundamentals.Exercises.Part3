def language_input():
    input1 = input("Choose Language  \n1. Spanish \n2. Dutch \n3. Chinese ")
    if input1 == "1":
        name1 = input("Bienvenida, ingresa tu nombre ")
        print("Saludos y hola! " + name1)
    elif input1 == "2":
        name2 = input("Welkom, vul uw naam in ")
        print("Groeten en hallo! " + name2)
    elif input1 == "3":
        name3 = input("歡迎您，請輸入您的名字 ")
        print("问候和你好 "+ name3)
    
  

language_input()
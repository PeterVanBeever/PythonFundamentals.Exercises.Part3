def name_input():
    input1 = input("Please enter your name")
    return input1

def language_input(name):
    greeting1 = "Bienvenida, ingresa tu nombre " + name
    greeting2 = "Welkom, vul uw naam in " + name
    greeting3 = "歡迎您，請輸入您的名字 " + name

    input1 = input("Choose Language  \n1. Spanish \n2. Dutch \n3. Chinese ")
    if input1 == "1":
        print(greeting1)
    elif input1 == "2":
        print(greeting2)
    elif input1 == "3":
        print(greeting3)


language_input(name_input())
#Урок 3. Задание 1.
#num = int(input("Введите число: "))
#if num % 2 == 0:
    #print("Число четное")
#else:
    #print("Число нечетное")

#Урок 3. Задание 2.
word = input("Введите слово: ")
vowels = "a,e,i,o,u"
no_letters = False
b = 0
for i in word:
    if i in vowels:
        b += 1

print(b)



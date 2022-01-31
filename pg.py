import random

input("This program generates easy-to-remember passwords by adding hints typed in by the user")
bruh = input("Enter a hint to added to your password. If there are multiple, seperate them with commas")
size = int(input("Enter password length"))

bruh2 = list(bruh)

ultrabruh = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0',"!","@","#","$","%","^","&",'*','(',')','_',"+",'-','=','{','}','|',':','<',"."]

lmfao = random.sample(ultrabruh, size)
str1 = ''
for i in lmfao:
    str1 += i

print("Password: ", str1)

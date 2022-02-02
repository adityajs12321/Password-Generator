import random

input("This program generates easy-to-remember passwords by adding hints typed in by the user")
bruh = input("Enter a hint to be added to your password. If there are multiple, separate them with commas")
size = int(input("Enter required password length"))

import nltk

bruh2 = list(bruh)

ultrabruh = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G',H','J','K','L','Z','X,'C','V','B','N','M','1','2','3','4','5','6','7','8','9','0',"!","@","#","$","%","^","&",'*','(',')','_',"+",'-','=','{','}','|',':','<',"."]

lmfao = random.sample(ultrabruh, size)

str1 = ''.join(lmfao)

print("Password: ", str1)
#JS sux
#prawnie sux

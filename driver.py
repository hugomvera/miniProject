from main import *

print("creating new class")


name = input("Enter your name: ")
print(name)

website = input("Enter your website: ")
print(website)

p1 = loginCredentials(name, website)

print("name: " +p1.name)
print("password: "+p1.password)
print("password: "+p1.website)
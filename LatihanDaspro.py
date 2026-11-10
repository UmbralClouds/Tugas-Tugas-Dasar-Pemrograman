# ALDRICH ZAVIER SULAEMAN
# RPL 1C
# 2607475

for i in range(0, 51, 5):
 
 print("Pass!", i)





























Animals = []

for i in range(3):
 Name = input("Insert animal name here: ")
 Animals.append(Name)

i = 0
a = 1

for Name in Animals:
 print(f"Animal {a} is {Name}")
 a += 1







NumberList = []

for i in range(3):
 times = int(input("insert your odd or even number: "))
 NumberList.append(times)

for times in NumberList:
 if times % 2 == 0:
  print(f"{times} is even!")
 else:
  print(f"{times} is odd")

multiples = []

for i in range(1, 51):
 if i % 3 == 0 or i % 5 == 0:
  print(i)

CorrectPassword = ["dasproRPL", "RPLfire!123"]

while CorrectPassword is False:
 input("Put in username: ")
 input("Put in password: ")
print("Correct! Welcome back!")
# penggunaan f string (dasar)
# x = "something"
# y = "suspicious"
# print(f"{x} + {y} = {x + y}")

# penggunaan input
# print("memulai scanning dengan ip: "+input("Masukkan ip yang ingin anda scan: "))

# mengubah string menjadi integer atau sebaliknya
# x=5
# y=" budak hitam?"
# print(str(x)+y)
# i="50"
# j=50
# print(f"aku mau {int(i)+j}!!!")

# print variabel yang berisi string ke console
# fname = input("masukkan nama depan anda: ")
# lname = input("masukkan nama belakang anda: ")
# print(f"Nama lengkap anda adalah: {fname} {lname}")

#if statement
# score = int(input("masukkan score anda: "))
# if score >= 90:
#     print("anda memiliki akreditasi A")
# elif score >= 80 and score <90:
#     print("anda memiliki akreditasi B")
# elif score >= 70 and score <80:
#     print("anda memiliki akreditasi C")
# elif score >= 60 and score <70:
#     print("anda memiliki akreditasi D")
# elif score >= 0 and score <60:
#     print("anda memiliki akreditasi E")
# else:
#     print("score tidak boleh minus")

#for loop
# bapak = ["Kandar", "Lukman", "Rahmat", "Helmi", "Khairi"]
#
# for nama in bapak:
#     print("nama bapak anak MI: " + nama)

# for num in range(0,11,2):
#     print(num)

#function
# angka = int(input("Masukkan angka : "))
# def lukman(x):
#     for num in range(1,100):
#         if num % 3 == 0 and num % 5 == 0:
#             print("Lukman")
#         elif num % 3 == 0:
#             print("Luk")
#         elif num % 5 == 0:
#             print("man")
#         else:
#             print(num)
#
# print("bersiaplah akan muncul lukman:")
# lukman(angka)

import random
pilihan = ["batu","gunting","kertas"]
print("permainan suit!")
pilihanuser = pilihan[int(input("yang mana pilihan kamu?\n1. batu\n2. Gunting\n3. Kertas\n"))-1]
angka =[1,2,3]
pilihanbot = random.choice(angka)
print(f"anda memilih: {pilihanuser}")
print(f"bot memilih: {pilihan[pilihanbot-1]}")
if(pilihanbot == 1 and pilihanuser == "gunting"):
    print("anda kalah")
elif(pilihanbot == 1 and pilihanuser == "kertas" ):
    print("anda menang")
elif(pilihanbot == 2 and pilihanuser == "batu"):
    print("anda menang")
elif(pilihanbot == 2 and pilihanuser == "kertas"):
    print("anda kalah")
elif(pilihanbot == 3 and pilihanuser == "batu"):
    print("anda kalah")
elif(pilihanbot == 3 and pilihanuser == "gunting"):
    print("anda menang")
elif(pilihan[pilihanbot-1] == pilihanuser):
    print("seri")
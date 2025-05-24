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
score = int(input("masukkan score anda: "))
if score >= 90:
    print("anda memiliki akreditasi A")
elif score >= 80 and score <90:
    print("anda memiliki akreditasi B")
elif score >= 70 and score <80:
    print("anda memiliki akreditasi C")
elif score >= 60 and score <70:
    print("anda memiliki akreditasi D")
elif score >= 0 and score <60:
    print("anda memiliki akreditasi E")
else:
    print("score tidak boleh minus")
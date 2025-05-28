import random

print("Selamat datang di tebak bahasa pemrograman")
bahasa = ["C++", "Python", "Java", "JavaScript", "C#", "PHP", "Ruby", "C", "Bash"]
pilihansaya = random.choice(bahasa)

displaybahasa = []
for huruf in pilihansaya:
    displaybahasa += "_"
print(displaybahasa)

print("Kira-kira bahasa pemrograman apa yang saya pikirkan?")
print(f"Nama bahasa pemrograman yang saya pikirkan mempunyai {len(pilihansaya)} huruf")

selesai = False
salah = 0
maksimal_salah = 3

while not selesai:
    tebakan = input("Masukkan tebakan huruf: ")
    benar = False

    for posisi in range(len(pilihansaya)):
        huruf = pilihansaya[posisi]
        if huruf.lower() == tebakan.lower():
            displaybahasa[posisi] = huruf
            benar = True

    if not benar:
        salah += 1
        print(f"Salah ke-{salah} dari maksimal {maksimal_salah}")

    print(displaybahasa)

    if "_" not in displaybahasa:
        print("Kamu Menang!!")
        selesai = True
    elif salah >= maksimal_salah:
        print("Kamu Kalah!! Kesempatan habis.")
        print(f"Jawabannya adalah: {pilihansaya}")
        selesai = True
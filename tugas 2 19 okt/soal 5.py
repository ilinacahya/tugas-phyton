
bawah = int(input("masukan nilai bawah: "))
atas = int(input("masukan nilai atas: "))

prima = []
for angka in range(bawah, atas + 1):
    if angka > 1:
        is_prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            is_prima = False
            break
    if is_prima:
        prima.append(angka)

print("bilangan prima: ", end=" ")
for angka in prima:
    print(angka, end=" ")

print()  
print("jumlah:", len(prima)) 
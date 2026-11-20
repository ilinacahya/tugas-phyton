#membuat pola segitiga bintang (perulangan bersarang)
#cetak juga versi terbaliknya

n = int(input("masukan n: "))

for i in range(1, n+1):
    print("*" * i)

#versi terbalik
print("\nversi terbalik: ")   
for i in range(n, 0, -1):
    print("*" * i)
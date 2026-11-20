#deret bilangan dan penjumlahan
#(perulangan)

deret = []
jumlah_semua = 0
jumlah_genap = 0


n =int(input("masukan n: "))

for i in range(1, n + 1):
         deret.append(i) 
         jumlah_semua += i
         if i % 2 == 0:
          jumlah_genap += i
        
print(f"deret: {deret}")
print(f"jumlah semua: {jumlah_semua}") 
print(f"jumlah genap: {jumlah_genap}")      

                 




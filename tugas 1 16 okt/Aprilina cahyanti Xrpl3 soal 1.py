# menghitung rata-rata nilai lulus spmb

#input
a = float(input("nilai MTK: "))
b = float(input("nilai B.IND: "))
c = float(input("nilai B.inggris: "))

#proses
nilai = (a + b + c) / 3


#output
if nilai >= 80:
   print("LULUS SPMB")

else :
   print("TIDAK LULUS SPMB")

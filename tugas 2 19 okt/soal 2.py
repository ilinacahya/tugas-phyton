#konversi nilai angka ke huruf
#(percabangan)

nilai = int(input("masukan nilai : "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai <= 100 or nilai >=85:
    print("Grade: A")
elif nilai >= 70:
    print("Grade: B")
elif nilai >=55:
    print("Grade: C")
elif nilai >= 40:
    print("Grade: D")
else:
    print("Grade: E")
     

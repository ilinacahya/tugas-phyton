#menentukan bilangan ganjil/genap dan positif/negatif 
#(percabangan)

bilangan = int(input("masukan bilangan : "))
if bilangan == 0:
    print("bilangan nol")
else:
    if bilangan > 0:
        print("bilangan positif")   
    else: 
        print("bilangan negatif")

if bilangan % 2 == 0:
    print("genap")    
else:
    print("ganjil")  

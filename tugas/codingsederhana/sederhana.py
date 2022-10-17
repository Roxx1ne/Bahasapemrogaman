# CONTOH CODING SEDERHANA
while True:
    
    pil = int(input("silahkan pilih nomor : "))
    if pil == 1:
        print("pilihan 1 = + ")
        def tambah():
            a = int(input("angka 1 : "))
            b = int(input("angka 2 : "))
            c = a + b 
            print (c)
        tambah()
    elif pil == 2:
        print("pilihan 2 =  - ")
        def kurang():
            a = int(input("angka 1 : "))
            b = int(input("angka 2 : "))
            c = a - b 
            print(c)
        kurang()
    elif pil == 3:
        print("pilihan 3 = operasi matematika ")
        def operasiMat():
            a = int(input("angka 1 : "))
            b = int(input("angka 2 : "))
            c = int(input("angka 3 : "))
            d  = a + b * c
            print(d)
        operasiMat()
    else :
        break
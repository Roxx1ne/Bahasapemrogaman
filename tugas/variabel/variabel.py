#contoh variabel
def func():
    B = "perkenalkan"
    N = " nama saya Naufal Aulio"
    print("selamat datang  " +  B  + N)
func()
#contoh variabel penjumlahan
def penjumlahan():
    angka1 = 20
    angka2 = 40 
    angka3 = angka1 + angka2
    print(angka3)
penjumlahan()

#definisi parameter
def data(nama, nim , jurusan):
    print(f"nama saya adalah " + nama + " Nim saya adalah " + nim + "jurusan saya " + jurusan)
data("Naufal Aulio" , "20210801018", "teknik informatika")

#contoh penjumlahan parameter
def segitiga (sisi, alas, tinggi):
    return sisi*sisi
def hitung (alas,tinggi):
    return 0.5 * alas * tinggi 
  

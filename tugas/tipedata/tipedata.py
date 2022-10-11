#string
a = "halo"
print(a)

#int 
b = 12
print(b)
print(type(b))
print("\n")

#float
c = 10.8
print (c)
print(type(c))
print("\n")

#tuple
d = (20,5,8,'a','b','c')
print(d)
print(type(d))
print("\n")

#contoh tuple
tuplecontoh = (3,2,1,8,'a','b','c')
print(tuplecontoh[0]) #ngakses array
print ('a' in tuplecontoh) #misalkan benar maka hasilnya true = nilai ada di dalam array 
print('x' in tuplecontoh) #misalkan salah maka hasilnya false = berati nilai x tidak ada di dalam array
print("\n")

#data complex
e = 1j
z = complex ('5-9j')
print(e)
print(z)
print(type(e))
print("\n")

#tipe data list
f = ["a","b","c"]
print(f)
print(type(f))
print("\n")

#contoh tipe data list
listContoh = [1,2,3,4,'a','b','c']
print(listContoh[0]) #ngakses array
print ("data sebelum diubah", listContoh)
print("\n")

#mengubah data pada indeks ke 2
listContoh[2] = 'halo'
print("data setelah diubah", listContoh)
print("\n")


#tipe data set
g = {"a","b","c"}
print(g)
print(type(g))
print("\n")

#contohset
setcontoh = {4,5,6,8,'a','b','c'} # output nya akan disusun seacara acak
print(setcontoh)
print("\n")

#contoh tipe data set yang memiliki nilai dobel
dobel = {4,4,5,1,2,6}
print(dobel) #otomatis angka 4 akan muncul sekali karena salah satu akan dihilangkan
print("\n")

#tipe data forzenset
h = frozenset({4,5,6})
#menambah angka pada array
h.add (3)
#menghapus angka pada array
h.remove(1) 
print (type(h)) # ini akan eror karena frpzensett tidak bisa menambah/menghapus angka dalam array
print("\n")

#tipe data boolean 
a = True 
c = False
print (a)
print (type(a))
print (c)
print(type(c))



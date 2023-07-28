import time

start_time = time.time()
integer = 78
float = 9,6
string = 'tulisan'

print('data =', integer) 
print('jenis =', type(integer))

print()
print('data =', float) 
print('jenis =', type(float))
print()
print('data =', string) 
print('jenis =', type(string))

# Tipe data khusus

print()
# Bilangan kompleks
data_complex = complex(7,8)
print('data =', data_complex) 
print('jenis =', type(data_complex))

# tipe data dari c

from ctypes import c_double

data_c = c_double(18.5)
print('data =', data_c) 
print('jenis =', type(data_c))


print()
print("Waktu dicapai:")
print(time.time() - start_time, "detik")
print("KALKULATOR")
print()

def plus(a,b):
	return a+b
def min(a,b):
	return a-b
def time(a,b):
	return a*b
def divide(a,b):
	return a/b

print('List imbol perhitungan\n       +\n       -\n       *\n       /')
print()

A = int(input("Masukkan angka pertama: "))
sim = str(input("Masukkan simbol perhitungan: "))
B = int(input("Masukkan angka pertama: "))
print()
if sim == '+':
	print('Hasil dari penjumlahan = ',plus(A,B))
elif sim == '-':
	print('Hasil dari penjumlahan = ',min(A,B))
elif sim == '*':
	print('Hasil dari penjumlahan = ',time(A,B))
elif sim == '/':
	print('Hasil dari penjumlahan = ',divide(A,B))


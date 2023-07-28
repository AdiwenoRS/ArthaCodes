nama = str(input('Masukkan nama anda: '))
sex = str(input('Anda pria/wanita?: '))

if sex == str('pria'):
    print('\nhalo bro', nama,"\n")
elif sex == str('wanita'):
    print('\nhalo sis', nama,'\n')
else:
    print('input salah')
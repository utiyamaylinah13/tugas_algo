tujuananda = ['jakarta','tanggerang','cikarang']
nama_penumpang = str(input('masukan nama ='))
booking_kursi = int(input('masukan nomor kursi = '))
nama_tujuan = str(input('masukan tujuan = '))
harga_tiket = int(input('masukan harga = '))
stok_tiket = int(input('masukan angka = '))


if nama_tujuan in tujuananda and harga_tiket >=300000 and stok_tiket <=5:
   print('anda mendapatkan tiket')
else:
   print('anda tidak mendapatkan tiket') 

if booking_kursi :
   print('tiket sudah dipesen')
else :
   print('belum ada pemesanan tiket')







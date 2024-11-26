data_limbah = {
    'lokasi' : {
        'nama_lokasi':'Area Kota 1',
        'jumlah_limbah' : {
            'plastik' : 500,
            'organik' : 300,
            'logam' : 200,
        }
    },
    'lokasi2' : {
        'nama_lokasi':'Area Kota 2',
        'jumlah_limbah' : {
            'plastik' : 700,
            'organik' : 400,
            'logam' : 250,
        }
    },
    'lokasi3' : {
        'nama_lokasi':'Area Kota 3',
        'jumlah_limbah' : {
            'plastik' : 600,
            'organik' : 350,
            'logam' : 300,
        }
    }
}

for i, j in data_limbah.items():
    print(i,j)

jumlah = data_limbah['lokasi2']['jumlah_limbah']
print(jumlah)

nama = data_limbah['lokasi3']['nama_lokasi']
print(nama)

for nama, jumlah in data_limbah.items():
    nama_lokasi = jumlah['nama_lokasi']
    jumlah_organik = jumlah['jumlah_limbah']['organik']
    jumlah_logam = jumlah['jumlah_limbah']['logam']

    if jumlah_organik > 400 or jumlah_logam > 250 :
        print(f"{nama_lokasi} memerlukan penanganan")
    else :
        print (f"{nama_lokasi} aman")
        
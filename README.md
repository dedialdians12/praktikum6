Nama  : Dedi Aldiansyah

Nim   : 312210452

Kelas : TI22B2

Tugas : Praktikum 5


1. Membuat dictionary data

2. Membuat menu pilihan (A)dd (E)dit (D)elete (S)earch (L)ist (Q)uit

A. Untuk pilihan A meninput Nama, Nim, Tugas, Uts dan Uas. jika nilai nama, nim, tugas, uts, dan uas kosong maka program ValueError dan meminta untuk input ulang. dan untuk data yg sudah di tambahkan menggunakan key nama.

Kode Program :

```
    elif c.lower() == 'a':
        print ("\nMasukan Data Mahasiswa")

        while (True):
            nama = input("NAMA : ")
            if nama == '':
                print ('Nama tidak boleh kosong')
            else:
                break
        while (True):
            try:
                nim  = int(input("NIM  : "))
                if nim == '':
                    print ('Masukan Nim dengan Angka')
            except ValueError:
                print ('Masukan Nim dengan Angka')
            else:
                break
        while (True):
            try:
                tugas  = int(input("TUGAS  : "))
                if tugas == '':
                    print ('Masukan TUGAS dengan Angka')
            except ValueError:
                print ('Masukan TUGAS dengan Angka')
            else:
                break
        while (True):
            try:
                uts  = int(input("UTS  : "))
                if uts == '':
                    print ('Masukan UTS dengan Angka')
            except ValueError:
                print ('Masukan UTS dengan Angka')
            else:
                break
        while (True):
            try:
                uas  = int(input("UAS  : "))
                if uas == '':
                    p('Masukan UAS dengan Angka')
            except ValueError:
                print ('Masukan UAS dengan Angka')
            else:
                break
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        data[nama] = [nama,nim,tugas,uts,uas,akhir]
```

Hasli program :

![image](https://user-images.githubusercontent.com/48305171/204148765-366b6009-e949-428b-b2f4-22745cf28862.png)


 
B. untuk pilihan E berfungsi untuk edit data yg sudah ada denagan nama sebagai key pencarian data, jika tidak sesuai maka data tidak di temukan. Lalu input pembaruan data dengan sesuai, jika ada yg kosong maka program ErorValue dan program meminta input ulang, dan jika sudah data sudah di perbarui

Kode Program :

```
 elif c.lower() == 'e':
        nama = input("Masukan nama untuk edit data : ")

        if nama in data.keys():
            del data[nama]
            print ("\nMasukan Pembaruan Data")

            while (True):
                nama = input("NAMA : ")
                if nama == '':
                    print ('Nama tidak boleh kosong')
                else:
                    break
            while (True):
                try:
                    nim = int(input("NIM  : "))
                    if nim == '':
                        print ('Masukan Nim dengan Angka')
                except ValueError:
                    print ('Masukan Nim dengan Angka')
                else:
                    break
            while (True):
                try:
                    tugas = int(input("TUGAS  : "))
                    if tugas == '':
                        print ('Masukan TUGAS dengan Angka')
                except ValueError:
                    print ('Masukan TUGAS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uts = int(input("UTS  : "))
                    if uts == '':
                        print ('Masukan UTS dengan Angka')
                except ValueError:
                    print ('Masukan UTS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uas = int(input("UAS  : "))
                    if uas == '':
                        print ('Masukan UAS dengan Angka')
                except ValueError:
                    print ('Masukan UAS dengan Angka')
                else:
                    break
            akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
            data[nama] = [nama, nim, tugas, uts, uas, akhir]

        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")
```

Hasil Program :

Data tersedia 

![image](https://user-images.githubusercontent.com/48305171/204149067-01149eaa-c909-4e80-9b94-2c9834955363.png)

Edit

![image](https://user-images.githubusercontent.com/48305171/204149079-5667075d-40c6-4539-9b53-4e017a03d3bd.png)

Sesudah di edit

![image](https://user-images.githubusercontent.com/48305171/204149139-178fa96f-d682-46ff-a53c-0996f9f8bae4.png)

C. Hapus data mengggunakan D dengan menggunakan pencarian nama

Kode Program :

```
    elif c.lower() == 'd':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print ("Data {} dihapus".format(nama))
        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


    else:
        print (" __________________________")
        print ("| Pilih opsi yang tersedia |")
        print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print ("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")
```

Hasil Program :

![image](https://user-images.githubusercontent.com/48305171/204149254-5ac417d1-2e6a-45f1-97a4-f3058d23ca65.png)

D. Mencari data menggunakan S dengan pencarian nama, jika tidak ada data (Data tidak di temukan)

Kode program :

```
    elif c.lower() == 's':
        nama = input("Masukan nama yang di cari : ")
        if nama in data.keys():

            print ("\n╔═════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╗")
            print ("║      NAMA       ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")
            print ("╠═════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")
            print ("║ {0:15} ║ {1:16} ║ {2:5} ║ {3:5} ║ {4:5} ║ {5:5} ║".format(nama, data[nama][1],data[nama][2], data[nama][3],data[nama][4], data[nama][5]))
            print ("╚═════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


    elif c.lower() == 'd':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print ("Data {} dihapus".format(nama))
        else:
            print (" ________________________")
            print ("| Data {} tidak ditemukan |".format(nama))
            print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
```

Hasil Program :

![image](https://user-images.githubusercontent.com/48305171/204150945-b3d3063d-530e-444a-bc0e-071955570f17.png)

E. Menampilkan data menggunakan L dengan data yg sudah tersedia

Kode program :

```
    elif c.lower() == 'l':
        print ("\n==========================================================================")
        print ("|========================= DAFTAR DATA MAHASISWA =========================|")
        print ("|=========================================================================|")
        print ("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print ("|==========================================================================")
        no = 1
        for tabel in data.values():
            print ("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0],tabel[1], tabel[2],tabel[3], tabel[4], tabel[5]))
            no += 1
        print ("===========================================================================")
```

Hasil program :

![image](https://user-images.githubusercontent.com/48305171/204151137-bbf76d3c-944c-406d-9b04-1c86774d0427.png)

F. Keluar menggunakan Q

Kode program :

```
    if c.lower() == 'q':
        break
```

Hasil program :

![image](https://user-images.githubusercontent.com/48305171/204151241-edda817f-ae56-4f12-9d72-a442fd335edf.png)

G. Jika menggunakan huruf lain diluar pilihan maka muncul (Pilih opsi yg tersedia)

Kode program :

```
    else:
        print (" __________________________")
        print ("| Pilih opsi yang tersedia |")
        print (" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print ("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")
```

Hasil program :

![image](https://user-images.githubusercontent.com/48305171/204151353-bbb742b6-84f8-4135-8c87-08d4f0e8a6dc.png)

Selesai, Terimakasih

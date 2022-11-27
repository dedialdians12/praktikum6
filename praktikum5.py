data = {}

print ("===========================================================================")
print ("|==================== PROGRAM INPUT DATA MAHASISWA =======================|")
print ("|=========================================================================|")
print ("|   (A)dd   |   (E)dit   |  (D)elete  |  (S)earch   |  (L)ist  |  (Q)uit  |")
print ("===========================================================================")

while True:

    c = input("\nPilih Opsi: ")


    if c.lower() == 'q':
        break

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
        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


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

        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


# EDIT DATA
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


    elif c.lower() == 's':
        nama = input("Masukan nama yang di cari : ")
        if nama in data.keys():

            print ("\n=====================================================================")
            print ("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
            print ("|====================================================================|")
            print ("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, data[nama][1],data[nama][2], data[nama][3],data[nama][4], data[nama][5]))
            print ("======================================================================")
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

        print ("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")



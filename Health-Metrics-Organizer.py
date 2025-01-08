import time
import os
import random
import pandas as pd
from datetime import date, datetime

#cek apakah file sudah tersedia atau belum
#jika sudah akan mereturn 1 dan jika belum akan mereturn 0
def cek_file(namafile) :
    try :
        cek = open(namafile, 'r')
        return 1
    except :
        return 0

#membuat file baru 
def buat_file(namafile) :
    while cek_file(namafile) == 0 :
        file = open(namafile, 'a+')
        file.close()
    return namafile

#memastikan pilihan berupa angka
def memastikan_pilihan(menu) :
    while True :
        try : 
            int(menu)
            break
        except :
            print('Maaf, menu yang Anda pilih tidak tersedia!')
            print('Silahkan pilih menu lainnya')
            menu = input('>> Pilih menu : ')
    return int(menu)

def petunjuk() :
    os.system('cls')
    petunjuk = open('petunjuk.txt', 'r')
    print(petunjuk.read())
    petunjuk.close()
    os.system('pause')

def tentang_kami() :
    os.system('cls')
    tentang = open('tentang.txt', 'r')
    print(tentang.read())
    tentang.close()
    os.system('pause')

#tampilan awal
def awal() :
    os.system('cls')
    print('--------------------------------------------------')
    print('>>>>> SELAMAT DATANG DI BMI & MAP CALCULATOR <<<<<')
    print('--------------------------------------------------')
    print('                             Tanggal : {0}'.format(date.today()))
    print('[1] Login')
    print('[2] Buat akun')
    print('[3] Petunjuk Penggunaan')
    print('[4] Tutup Program')
    print('[5] Tentang Kami')
    menu = input('>> Pilih Menu : ')
    menu = memastikan_pilihan(menu)
    if menu == 1 :
        login()
    elif menu == 2 :
        buat_akun()
    elif menu == 3 :
        petunjuk()
        awal()
    elif menu == 4 :
        os.system('cls')
        print('\n\n\n\t\t\t ^o^ Terima Kasih ^o^\n\n\n')
        quit()
    elif menu == 5 :
        tentang_kami()
        awal()
    else :
        print('Menu yang Anda pilih Tidak tersedia!\nSilahkan pilih menu lain!')
        time.sleep(3)
        os.system('cls')
        awal()

def login() :
    i = 0
    os.system('cls')
    print('----------------------------------')
    print('>>>>>>>>>>> MENU LOGIN <<<<<<<<<<<')
    print('----------------------------------')
    ID       = input('Masukan ID Anda       : ')
    password = input('Masukan password Anda : ')
    try :
        open('listID.txt', 'r')
        open('listPass.txt', 'r')
    except :
        print('ID Anda tidak terdaftar, silahkan daftarkan akun Anda!')
        os.system('pause')
        awal()
    id = open('listID.txt', 'r')
    pw = open('listPass.txt', 'r')
    flag = 0
    j = 0
    for lineID in id :
        if lineID == ID+'\n' :
            flag = 1
            break
        i+=1
    if flag == 1 : 
        for linePass in pw :
            while i > 0 :
                i-=1
                continue
            if linePass == password+'\n' :
                print('Log in berhasil!')
                flag = 2
                id.close()
                pw.close()
                os.system('pause')
                break
            
    while flag == 1 :
        id.close()
        pw.close()
        print('Password yang Anda masukan, salah! Silahkan masukan kembali password')
        os.system('pause')
        awal()

    if flag == 2 :
        menu_utama(ID)
    else :
        print('ID Anda tidak terdaftar, silahkan daftarkan akun Anda!')
        id.close()
        pw.close()
        os.system('pause')
        awal()

def buat_akun() :
    os.system('cls')
    print('------------------------------------')
    print('>>           Buat Akun            <<')
    print('------------------------------------')
    nama = input('Masukan Nama          : ')
    jk = input('Masukan Jenis Kelamin : ')
    umur = input('Masukan Umur          : ')
    
    #menambahkan password
    password0 = input('Masukan Password Akun : ')
    password1 = input('Ulangi Password       : ')
    while password0!=password1 :
        print('Password yang Anda masukan salah!')
        password0 = input('Masukan Password Akun : ')
        password1 = input('Ulangi Password       : ')
    
    #mencetak ID secara random
    ID = IDgenerator()

    #melakukan perulangan jika ID yang dihasilkan telah ada sebelumnya, kemudian menyimpan nilai ID ke daftar ID
    while(daftarID(ID) == 0) :
       ID = IDgenerator
    
    #menambahkan password ke daftar password
    daftarPass(password0)
    profil =  [ID, password0,nama ,umur,jk, datetime.now().year]
    columns = ['ID', 'Password', 'Nama', 'Umur', 'Jenis Kelamin', 'Tahun']
    namafile = ID+'profil'+'.csv'
    fileprofil = pd.DataFrame(data = profil, index= columns).T
    fileprofil.to_csv(namafile, index=False)
    print("Memproses . . .")
    time.sleep(3)
    print('\nSelamat! Akun Anda berhasil dibuat!\nID ANDA : ', ID)
    print('\nJangan lupa untuk mengingat ID dan password Anda\nSilahkan log in')
    os.system('pause')
    awal()

#generate random ID 
def IDgenerator() :
    ID = ''
    for i in range(5) :
        ID = ID + str(random.randint(0, 9))
    return ID

#cek apakah ID telah digunakan atau belum, jika belum ID akan digunakan dan dimasukan ke file
def daftarID(ID) :
    listID = buat_file('listID.txt')
    listID = open(listID, 'a+')
    if ID not in listID :
        listID.write(ID+'\n')
        listID.close()
    else :
        listID.close()
        return 0

#menambahkan password user ke file
def daftarPass(password) : 
    listPass = buat_file('listPass.txt')
    listPass = open(listPass, 'a+')
    listPass.write(password+'\n')
    listPass.close()

#menggabungkan 2 dataframe menjadi 1 dataframe
#mengubah data frame ke 
def gabung_df(file1, file2) :
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.concat([df1, df2], ignore_index=True)
    df3.to_csv(file1, index=False)

#menampilkan menu utama
#menu setelah log in berhasil
def menu_utama(ID) :
    os.system('cls')
    #membuat file riwayat jik belum ada
    if cek_file(ID+'riwayat'+'.csv') == 0 :
        columns = ['Tanggal','Berat Badan','Tinggi Badan','Nilai BMI', 'Keterangan BMI', 'Tekanan Darah Sistolik', 'Tekanan Darah Diastolik','Nilai MAP', 'Keterangan MAP']
        isi = ['-']*9
        riwayat = pd.DataFrame(data=isi, index=columns).T
        riwayat.to_csv(ID+'riwayat_temp.csv', index=False)
        riwayat = riwayat.drop(0)
        riwayat.to_csv(ID+'riwayat'+'.csv',index=False)
        

    #membuka file riwayat
    riwayat = pd.read_csv(ID+'riwayat'+'.csv')
    profil = pd.read_csv(ID+'profil'+'.csv')
    nama = profil['Nama'].to_string(index=False)
    print('---------------------------------------------------')
    print('Selamat Datang, ',nama,'. Silahkan pilih menu berikut!',sep='')
    print('---------------------------------------------------')
    print("[1] Masukan Data dan Perhitungan")
    print("[2] Lihat Riwayat Kesehatan")
    print("[3] Log Out")
    menu = input('>> Pilih menu : ')
    menu = memastikan_pilihan(menu)
    if menu == 3 :
        os.system('cls')
        print('\n\n\n\t\t\tTerima Kasih ^o^\n\n\n')
        os.system('pause')
        awal()
    elif menu == 2 :
        riwayat_kesehatan(ID)
        menu_utama(ID)
    elif menu == 1 :
        menu_program(ID)
    else :
        print('Menu yang Anda pilih Tidak tersedia!\nSilahkan pilih menu lain!')
        time.sleep(5)
        os.system('cls')
        menu_utama()

def tampil_profil(ID) :
    profil = pd.read_csv(ID+'profil.csv')
    print('ID            : ', ID)
    print('Nama          : ', profil['Nama'].to_string(index=False))
    print('Jenis Kelamin : ', profil['Jenis Kelamin'].to_string(index=False))
    print('Umur          : ', int(profil['Umur'].to_string(index=False))+datetime.now().year - int(profil['Tahun'].to_string(index=False)))
    print('Tanggal       : ', date.today())

def riwayat_kesehatan(ID) :
    os.system('cls')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('>>                                                           Riwayat Kesehatan                                                              <<')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    tampil_profil(ID)
    print('----------------------------------------------------------------------------------------------------------------------------------------------')

    riwayat = pd.read_csv(ID+'riwayat.csv')
    print(riwayat.to_string(index=False))
    print('----------------------------------------------------------------------------------------------------------------------------------------------')

    print('\nAnda akan di arahkan ke [Menu Utama]')
    os.system('pause')
    
def menu_program(ID) :
    os.system('cls')
    print('---------------------------------')
    print(">>>>>>>>> Menu Program <<<<<<<<<<")
    print('---------------------------------')
    print("[1] Hitung BMI")
    print("[2] HItung MAP")
    print('[3] Kembali ke Menu Utama')
    menu = input('>> Pilih Menu : ')
    menu = memastikan_pilihan(menu)
    if menu == 1 :
        bmi(ID)
        menu_program(ID)
    elif menu == 2 :
        MAP(ID)
        menu_program(ID)
    elif menu == 3 :
        file1 = ID+'riwayat.csv'
        file2 = ID+'riwayat_temp.csv'
        gabung_df(file1, file2)
        menu_utama(ID)

def bmi(ID) :
    os.system('cls')
    riwayat = pd.read_csv(ID+'riwayat_temp'+'.csv')
    bb = 0
    print('------------------------------------------------')
    print('>>      Program menghitung nilai BMI          <<')
    print('------------------------------------------------')
    tampil_profil(ID)
    print('------------------------------------------------')
    print('Nilai BMI normal ada di antara 18.5 - 25 kg/m^2')
    bb = input("Masukan berat badan (kg) Anda      : ")
    tb = input("Masukan tinggi badan (m) yang Anda : ")
    while True :
        try :
            float(bb)
            float(tb)
            riwayat['Tinggi Badan'] = tb
            riwayat['Berat Badan'] = bb
            break
        except :
            print("\nMasukan berat badan dan tinggi badan dalam angka!")
            bb = input("Masukan berat badan (kg) Anda : ")
            tb = input("Masukan tinggi badan (m) Anda : ")
    bmi = float(bb)/(float(tb)*float(tb))
    bmi = round(bmi, 2)
    print('-------------------------------------------------')
    print('Nilai BMI Anda : ', bmi)
    riwayat['Tanggal'] = date.today()
    riwayat['Nilai BMI'] = str(bmi)
    riwayat['Keterangan BMI'] = kls_bmi(bmi)
    if bmi<18.5 or bmi>25 : 
        bbIdeal(float(bb), float(tb))
    riwayat.to_csv(ID+'riwayat_temp'+'.csv', index=False)
    print('\nAnda akan diarahkan kembali ke [Menu Program]')
    os.system('pause')

#menentukan range nilai bmi dan klasifikasinya
def kls_bmi(nilaiBMI) :
    teks = ''
    if nilaiBMI <= 18.5 :         
        print("Berat badan Anda kurang")   
        return "Berat badan kurang"
    elif nilaiBMI < 25 and nilaiBMI > 18.5 :
        print("Berat badan Anda ideal")
        return "Ideal"
    elif nilaiBMI < 30 and nilaiBMI >= 25 :
        print("Berat badan Anda termasuk terlebih")
        return "Berat berlebih"
    else :
        print("Anda termasuk katagori obesitas")
        return 'Obesitas'

#fungi tambahan yang akan menampilkan perkiraan berat badan yang ideal 
def bbIdeal(bb, tb) :
    ideal1 = 25*tb*tb
    ideal1 = round(ideal1, 2)
    ideal2 = 18.5*tb*tb
    ideal2 = round(ideal2, 2)
    
    print('\nCatatan :\n- Agar ideal berat badan Anda harus berada di antara', ideal2, '-', ideal1, 'kg')
    if bb<ideal2 :            
        print('- Anda dapat menambah berat badan sebesar', round(ideal2-bb, 2),'kg')
    else :
        print('- Anda dapat mengurangi berat badan sebesar', round(bb-ideal1, 2),'kg')

#fungsi menentukan nilai map
def hitung_MAP(sb, db) :
    return (2*sb+db)/3

#fungsi map
def MAP(ID) :
    os.system('cls')
    #membuka dataframe yang nantinya akan berisi update nilai dari data yang dimasukan
    riwayat = pd.read_csv(ID+'riwayat_temp'+'.csv')
    sb = 0
    print('--------------------------------------------------------------')
    print(">>             Program menghitung nilai MAP                 <<")
    print('--------------------------------------------------------------')
    tampil_profil(ID)
    print('------------------------------------------------')
    print('Tekanan darah normal memiliki nilai MAP sebesar 70 - 100 mmHg')
    sb = input("Masukan tekanan darah sistolik  Anda     : ")
    db = input("Masukan tekanan darah diastolik Anda     : ")
    while True :
        try :
            float(sb)
            float(db)
            riwayat['Tekanan Darah Sistolik'] = sb
            riwayat['Tekanan Darah Diastolik'] = db
            break
        except :
            print("\nMasukan tekanan darah sistolik dan diastolik dalam angka!")
            sb = input("Masukan tekanan darah sistolik  Anda     : ")
            db = input("Masukan tekanan darah diastolik Anda     : ")
    map = hitung_MAP(float(sb), float(db))
    map = round(map, 2)
    riwayat['Nilai MAP'] = str(map)
    riwayat['Tanggal'] = date.today()
    print('--------------------------------------------------------------')
    print('Nilai MAP Anda : ', map)
    riwayat['Keterangan MAP'] = kls_MAP(int(sb), int(db))
    print('\nAnda akan diarahkan kembali ke [Menu Program]')
    riwayat.to_csv(ID+'riwayat_temp'+'.csv', index=False)
    os.system('pause')

def kls_MAP(sb, db) :
    if sb < 140 and sb >= 120 or db < 90 and db >= 80 :
        print('Tekanan darah anda termasuk \'Prahipertensi\'.\n\nCatatan : Anda disarankan melakukan pemeriksaan jika memiliki keluhan')
        return 'Prahipertensi'
    elif sb < 160 and sb >= 140 or db < 100 and db >= 90 :
        print('Tekanan darah Anda termasuk \'Hipertensi derajat 1\'.\n\nCatatan : Silahkan melakukan pemeriksaan ke dokter!')
        return 'Hipertensi derajat 1'    
    elif sb >= 160 or db >= 100 :
        print('Tekanan darah Anda termasuk \'Hipertensi derajat 2\'.\n\nCatatan : Segera lakukan pemeriksaan ke dokter!')
        return 'Hipertensi derajat 2'
    elif sb < 90 or db < 60 :
        print('Tekanan darah Anda termasuk \'Hipotensi\'.\n\nCatatan : Segera lakukan pemeriksaan jika mengalami gejala lain')
        return 'Hipotensi'
    else :
        print('Tekanan darah Anda \'Normal\'.\n\nCatatan : Tetap jaga kondisi tubuh')
        return 'Normal'

#menjalankan program
awal()
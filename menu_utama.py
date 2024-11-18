import pembukuan_UMKM
import pendaftaran_UMKM
import pendaftaran_pelatihan
import webbrowser


while True:
    try:
        print("========== SAHABAT USAHA ==========")
        print("[1] Level Up Your Enterpreunurship Skills !!!")
        print("[2] Create Your Own Shop !!!")
        print("[3] Manage your shop and become a successful entrepreneur!!!")
        print("[4] Exit")
        pilihan_pengguna = int(input("Masukkan fitur yang ingin diakses: "))
        if pilihan_pengguna == 1:
            pendaftaran_pelatihan.menu_registrasi_pelatihan_kewirausahaan()
        elif pilihan_pengguna == 2:
            pendaftaran_UMKM.menu_utama_registrasi_umkm()
        elif pilihan_pengguna == 3:
            pembukuan_UMKM.menu_utama_fitur_pembukuan()
        elif pilihan_pengguna == 4:
            webbrowser.open("https://fauzan-putra.github.io/ucapan-terima-kasih/")
            exit()
        else:
            print("Pilihan pengguna tidak valid")
    except ValueError:
        print("Input harus berupa angka. Coba lagi !!!")
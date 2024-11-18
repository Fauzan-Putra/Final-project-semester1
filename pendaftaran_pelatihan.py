def pengisian_data_pelatihan():
    daftar_pertanyaan = [
        "Nama lengkap",
        "Alamat",
        "Email",
        "Nomor telepon",
        "Memiliki pengalaman berwirausaha [Ya/Tidak]",
        "Rencana jenis usaha [Barang/Jasa]",
        "Jelaskan secara singkat komitmen dan motivasi anda berwirausaha"
    ]
    respon_pengguna = {}

    for pertanyaan in daftar_pertanyaan:
        jawaban = input(f"{pertanyaan}: ")
        respon_pengguna[pertanyaan] = jawaban

def menu_registrasi_pelatihan_kewirausahaan():
    print("========== Pendaftaran Pelatihan Kewiraushaan ==========")
    print("Isi pertanyaan dibawah ini: ")
    pengisian_data_pelatihan()
    print("\n")
    print("Terima kasih telah mendaftar melalui program sahabat usaha !!!")
    print("Permintaan anda akan segera diverifikasi dan diproses setelah anda mengupload beberapa berkas pendukung. ")
    print("\n")

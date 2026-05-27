# Soal: Teks Proklamasi

# Diberikan sebuah string teks Proklamasi yang asli
teks_asli = "Kami Bangsa Indonesia dengan ini menjatakan kemerdekaan Indonesia. Hal-hal jang mengenaik pemindahan kekoeasaan d.l.l diselenggarakan dengan tjara seksama dan dala tempo jang sesingkat-singkatnja. Djakarta, hari 17 boelan 8 tahoen 05 Atas nama bangsa Indonesia Soekarno/Hatta"

# Pertanyaan
# Diminta membuat fungsi dengan nama cekFormat yang hanya memiliki satu parameter bernama teks.
# Fungsi ini bakalan cek parameter teks, apakah sudah sesuai dengan teks proklamasi asli
# Akan mengembalikan kata yang salah dalam sebuah list, jika benar semua return []

# Example
# Kami Bangsa Indonesia dengn ini menyatakan kemerdekaan Indonesia.", fungsi harus mengembalikan array ["menyatakan", "dengn"]


def cekFormat(teks):

    # Split teks dan teks_asli menjadi list kata kata
    kata_teks = teks.split()
    kata_asli = teks_asli.split()

    # Variable list untuk menyimpan kata yang salah
    kata_salah = []

    # Bandingkan setiap kata dalam teks dengan teks asli
    for i in range(len(kata_teks)):
        if i >= len(kata_asli) or kata_teks[i] != kata_asli[i]:
            kata_salah.append(kata_teks[i])

    return kata_salah


teks_proklamasi = "Kami Bangsa Indonesia dengn ini menyatakan kemerdekaan Indonesia."
hasil = cekFormat(teks_proklamasi)
print(hasil)

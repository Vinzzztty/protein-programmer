# Protein bagi Programmer

> Semakin makan protein, semakin handal kamu sebagai programmer.

[LeetCode Profile](https://leetcode.com/u/Vinzzztty/)

Repository ini jadi markas latihan untuk mengasah ulang logic, pattern recognition, dan problem solving. Fokus utamanya bukan mengejar jumlah soal, tapi membangun fondasi algoritma lewat repetisi yang sadar dan terukur.

## Cara Pakai

Workflow utama sekarang ada di [docs/leetcode-workflow.md](docs/leetcode-workflow.md).

Kalau kamu mau lihat versi visualnya dulu, buka section `Visual Flowchart` di dokumen itu.

Quick start untuk satu soal baru:

1. Pilih satu pattern aktif dari roadmap.
2. Scaffold folder soal:

```bash
python3 scripts/new_leetcode_problem.py 704 "Binary Search" --pattern "Binary Search" --difficulty Easy
```

Untuk soal lama yang sedang masuk ulang ke workflow, tambahkan `--stage Review`.

3. Kerjakan `Attempt 0` dan `Attempt 1`.
4. Rapikan solusi final ke `solution.py`.
5. Isi `notes.md` dan update tracker Notion di hari yang sama.

## Struktur Repo

- `python-leetcode/`: kumpulan soal algoritma Python.
- `30-days-pandas-leetcode/`: track Pandas dari LeetCode.
- `introduction-pandas/`: latihan dasar Pandas.
- `docs/leetcode-workflow.md`: sumber kebenaran untuk workflow belajar.
- `scripts/new_leetcode_problem.py`: scaffold satu folder soal lengkap dengan notes dan file repetisi.

## Prinsip Belajar

- Satu soal = satu folder, satu catatan utama, beberapa repetisi.
- Repetisi lebih penting daripada quantity.
- Pattern dipelajari berurutan, bukan random.
- Python jadi bahasa utama sampai fondasi stabil.

## Python yang Dipakai

Repository ini menargetkan Python 3.12 sesuai [python-version.txt](python-version.txt).

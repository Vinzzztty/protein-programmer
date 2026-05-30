# 13. Roman to Integer

- Difficulty: Easy
- Pattern: Has Table
- Stage: New
- Repo Path: `python-leetcode/13-roman-to-integer`
- Created At: 2026-05-28

## Problem summary

- Tulis ulang soal ini dengan bahasamu sendiri.
- Catat input, output, constraint, dan contoh penting.

Diberikan 7 simbol romawi: I, V, X, L, C, D dan M

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Kondisi
II = 2, karena dulis dua kali bersamaan
XXVII = 27 -> XX + V + II (10+10 + 5 + 1+1)

Kondisi pada romawi 4 itu IV bukan IIII, karena satu angka sebelum simbol 5 (V) itu dikurangi untuk membentuk angka 4

Input s = "III"
Output = 3

Input s = "LVIII"
Output = 58



## Pattern

- Pattern utama:
- Kenapa pattern ini cocok:
- Pattern lain yang sempat kepikiran:

## Brute force idea

- Ide pertama yang paling natural:
- Kenapa terlalu lambat atau terlalu ribet:

## Final insight

- Insight yang membuka jalan ke solusi final:
- Invariant atau rule penting yang harus diingat:

## Mistakes made

- Bug pertama:
- Miskonsepsi utama:
- Hal yang ingin dihindari di repetisi berikutnya:

## Complexity

- Time:
- Space:

## Repetition log

| Date | Repetition | Time finished | Need hint? | Main bug or mistake | Confidence (1-5) | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-28 | Attempt 0 |  |  |  |  | 2026-05-28 |
| 2026-05-28 | R1 |  |  |  |  | 2026-05-29 |
| 2026-05-29 | R2 |  |  |  |  | 2026-06-01 |
| 2026-06-01 | R3 |  |  |  |  | 2026-06-08 if masih goyah |

## Next review

- Current target: 2026-05-28
- Rule:
  - R1 di hari yang sama
  - R2 +1 hari
  - R3 +3 sampai 5 hari
  - R4 +7 sampai 14 hari kalau masih goyah

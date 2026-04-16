========================================
  PROYEK WEBSITE BIOGRAFI ALI SADIKIN
========================================

STRUKTUR FOLDER:
─────────────────
ali_sadikin_project/
│
├── ali_sadikin_biography.html   ← File utama website
│
├── foto/                        ← Taruh foto-foto di sini
│   ├── sketsa_ali_sadikin.jpg
│   └── ilustrasi_ali_sadikin.jpg
│
├── embed_foto.py                ← Script Python untuk embed foto ke HTML
│
└── README.txt                   ← Panduan ini


========================================
  CARA NAMBAHIN / GANTI FOTO
========================================

LANGKAH 1 — Taruh foto baru di folder "foto/"
  Contoh: foto/foto_baru.jpg

LANGKAH 2 — Jalankan script embed_foto.py
  Buka terminal/command prompt di folder ini, lalu ketik:

    python embed_foto.py

  Script akan tanya foto mana yang mau di-embed dan
  di slide/elemen mana mau ditaruh.

ATAU — Edit manual di ali_sadikin_biography.html:
  Cari tag <img> yang mau diganti, lalu jalankan:

    python embed_foto.py --file foto/foto_baru.jpg

  Copy hasilnya (teks panjang base64) dan tempel
  menggantikan teks base64 yang lama di HTML.


========================================
  CARA BUKA WEBSITE
========================================

Cukup double-klik file:
  ali_sadikin_biography.html

Bisa dibuka di Chrome, Firefox, Safari, Edge.
Bisa di HP, Tablet, maupun Laptop.

Navigasi:
  - Klik tombol ← → di bawah layar
  - Tekan tombol panah keyboard
  - Geser kiri/kanan (di HP/Tablet)


========================================
  CATATAN
========================================

- Semua foto sudah di-embed langsung ke dalam HTML
  jadi cukup kirim 1 file HTML saja, foto tidak akan hilang.
- Jika ingin ganti foto, gunakan embed_foto.py
  supaya foto baru juga ikut tersimpan di dalam HTML.

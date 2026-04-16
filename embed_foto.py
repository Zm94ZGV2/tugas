"""
========================================
  EMBED FOTO KE HTML — Ali Sadikin
========================================

Script ini mengubah file foto (JPG/PNG) menjadi base64
lalu menyimpannya supaya bisa ditempel langsung ke HTML.

CARA PAKAI:
  python embed_foto.py
  → Mode interaktif, ikuti petunjuk di layar

  python embed_foto.py --file foto/nama_foto.jpg
  → Langsung embed 1 foto, hasil dicetak ke terminal

  python embed_foto.py --file foto/nama_foto.jpg --output hasil.txt
  → Simpan hasil base64 ke file teks
"""

import base64
import os
import sys
import argparse


def foto_ke_base64(path_foto: str) -> str:
    """Ubah file foto jadi string base64."""
    with open(path_foto, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return data


def deteksi_mime(path_foto: str) -> str:
    """Deteksi tipe MIME dari ekstensi file."""
    ext = os.path.splitext(path_foto)[1].lower()
    mime_map = {
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png":  "image/png",
        ".gif":  "image/gif",
        ".webp": "image/webp",
    }
    return mime_map.get(ext, "image/jpeg")


def buat_tag_img(path_foto: str, style: str = "", alt: str = "foto") -> str:
    """Buat tag <img> lengkap dengan base64 embedded."""
    b64 = foto_ke_base64(path_foto)
    mime = deteksi_mime(path_foto)
    src = f"data:{mime};base64,{b64}"
    style_attr = f' style="{style}"' if style else ""
    return f'<img src="{src}"{style_attr} alt="{alt}">'


def ganti_foto_di_html(path_html: str, cari_alt: str, path_foto_baru: str, style: str = ""):
    """
    Ganti foto di HTML berdasarkan atribut alt-nya.
    
    Contoh: kalau ada <img ... alt="sketsa_ali"> di HTML,
    panggil fungsi ini dengan cari_alt="sketsa_ali"
    """
    with open(path_html, "r", encoding="utf-8") as f:
        html = f.read()

    tag_baru = buat_tag_img(path_foto_baru, style=style, alt=cari_alt)

    # Cari dan ganti tag img dengan alt yang sesuai
    import re
    pattern = rf'<img[^>]*alt="{re.escape(cari_alt)}"[^>]*>'
    matches = re.findall(pattern, html)

    if not matches:
        print(f"❌ Tidak ditemukan <img> dengan alt=\"{cari_alt}\" di {path_html}")
        return False

    html_baru = re.sub(pattern, tag_baru, html)

    with open(path_html, "w", encoding="utf-8") as f:
        f.write(html_baru)

    print(f"✅ Berhasil ganti foto dengan alt=\"{cari_alt}\" di {path_html}")
    return True


def mode_interaktif():
    """Mode tanya-jawab untuk embed foto."""
    print("=" * 50)
    print("  EMBED FOTO KE HTML — Mode Interaktif")
    print("=" * 50)

    # Pilih foto
    print("\n📁 Foto yang tersedia di folder 'foto/':")
    foto_dir = "foto"
    if os.path.exists(foto_dir):
        files = [f for f in os.listdir(foto_dir)
                 if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif"))]
        for i, f in enumerate(files, 1):
            size_kb = os.path.getsize(os.path.join(foto_dir, f)) // 1024
            print(f"  {i}. {f} ({size_kb} KB)")
    else:
        print("  (folder 'foto/' kosong atau tidak ada)")
        files = []

    print()
    path_foto = input("Masukkan path foto (contoh: foto/nama.jpg): ").strip()

    if not os.path.exists(path_foto):
        print(f"❌ File tidak ditemukan: {path_foto}")
        return

    # Pilih mode output
    print("\nMau dipakai untuk apa?")
    print("  1. Cetak tag <img> lengkap ke terminal (untuk copy-paste ke HTML)")
    print("  2. Simpan base64-nya ke file .txt")
    print("  3. Ganti foto di ali_sadikin_biography.html berdasarkan atribut alt")
    pilihan = input("\nPilih (1/2/3): ").strip()

    if pilihan == "1":
        style = input("Style CSS (kosongkan = pakai default): ").strip()
        if not style:
            style = "width:100%; height:100%; object-fit:cover; border-radius:10px;"
        alt = input("Teks alt (contoh: foto_ali): ").strip() or "foto"
        tag = buat_tag_img(path_foto, style=style, alt=alt)
        print("\n" + "=" * 50)
        print("✅ Tempel kode ini ke HTML kamu:")
        print("=" * 50)
        print(tag[:200] + "...[base64 panjang]..." + tag[-50:])
        print("\n(Tag lengkap tersimpan di 'hasil_embed.txt')")
        with open("hasil_embed.txt", "w") as f:
            f.write(tag)

    elif pilihan == "2":
        b64 = foto_ke_base64(path_foto)
        mime = deteksi_mime(path_foto)
        output = f"data:{mime};base64,{b64}"
        out_file = "hasil_base64.txt"
        with open(out_file, "w") as f:
            f.write(output)
        print(f"✅ Base64 disimpan ke '{out_file}' ({len(b64)} karakter)")

    elif pilihan == "3":
        path_html = input("Path HTML (kosongkan = ali_sadikin_biography.html): ").strip()
        if not path_html:
            path_html = "ali_sadikin_biography.html"
        cari_alt = input("Atribut alt dari <img> yang mau diganti: ").strip()
        style = input("Style CSS baru (kosongkan = pakai yang lama): ").strip()
        ganti_foto_di_html(path_html, cari_alt, path_foto, style)
    else:
        print("❌ Pilihan tidak valid.")


def main():
    parser = argparse.ArgumentParser(description="Embed foto ke HTML sebagai base64")
    parser.add_argument("--file", help="Path ke file foto")
    parser.add_argument("--output", help="Simpan hasil ke file ini")
    parser.add_argument("--alt", default="foto", help="Teks alt untuk tag img")
    parser.add_argument("--style", default="width:100%;height:100%;object-fit:cover;border-radius:10px;",
                        help="Style CSS untuk tag img")
    args = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print(f"❌ File tidak ditemukan: {args.file}")
            sys.exit(1)

        tag = buat_tag_img(args.file, style=args.style, alt=args.alt)

        if args.output:
            with open(args.output, "w") as f:
                f.write(tag)
            print(f"✅ Disimpan ke {args.output}")
        else:
            # Tampilkan versi pendek di terminal
            preview = tag[:120] + "...[base64]..." + tag[-30:]
            print(preview)
            with open("hasil_embed.txt", "w") as f:
                f.write(tag)
            print("\n✅ Tag lengkap disimpan di 'hasil_embed.txt'")
    else:
        mode_interaktif()


if __name__ == "__main__":
    main()

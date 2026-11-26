[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · **Bahasa Indonesia** · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Meja kerja Linux asli untuk kamera Video4Linux.**

Pilih webcam, lihat pratinjau langsungnya, pilih mode pengambilan dan sesuaikan kontrol yang diekspos oleh driver kamera.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Status: perkembangan awal">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 dan libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer dan V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera , meja kerja kamera Linux asli. Gambar menunjukkan prototipe desain interaktif.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Jalankan di Linux"></a>&nbsp; & nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Lihat desainnya"></a>&nbsp; & nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Lihat peta jalan"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Penemuan kamera, pratinjau langsung, mode pengambilan, kontrol perangkat keras, diagnostik, dan penampilan">

<details>
<summary><b>Lebih lanjut tentang fiturnya</b></summary>

- **Kamera.** Pilih perangkat V4L2 dan pindai ulang setelah menghubungkan atau melepaskan kamera.
- **Pratinjau langsung.** Mulai dan hentikan aliran lokal dan lihat tingkat penangkapan yang diukur di sumbernya. Jika tersedia, aplikasi melukis bingkai dengan wastafel GStreamer GTK 4. Ini juga mendukung fallback tekstur GTK yang dibatasi.
- **Mode pengambilan.** Gunakan negosiasi otomatis atau pilih kombinasi resolusi, format piksel, dan kecepatan bingkai yang diiklankan. Ubah mode antar sesi pratinjau.
- **Kontrol perangkat keras.** Edit kontrol numerik, sakelar, dan menu yang dilaporkan oleh pengemudi. Perubahan dikirim ke driver saat Anda membuatnya.
- **Diagnostik dan penampilan.** Periksa akses perangkat, dependensi yang hilang, dan kesalahan pratinjau. Pengaturan menawarkan sistem, tampilan terang dan gelap.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Pilih perangkat dan mode, mulai pratinjau, lalu sesuaikan kontrol kamera yang didukung">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Status pratinjau: berhenti, memulai, menangkap, dan terputus">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Pola pengujian sintetis pada 30, 60 atau 120 FPS, ditambah tiga mode tampilan asli">

## Mulai cepat

1. Hubungkan webcam dan pilih **Perangkat**. Gunakan tombol segarkan jika dicolokkan setelah membuka aplikasi.
2. Open Camera memilih 60 FPS saat kamera melaporkannya, atau 59.94 FPS saat itu adalah satu-satunya mode mendekati 60. Memilih **Otomatis** untuk membiarkan pengemudi bernegosiasi atau memilih salah satu kombinasi yang dilaporkan.
3. Klik **Mulai pratinjau**. Pembacaan FPS mengukur frame yang datang dari sumbernya. Kecepatan ini dapat berbeda dari kecepatan yang diminta dan tidak mengukur penyegaran monitor.
4. Sesuaikan kontrol yang dipaparkan pengemudi Anda saat menonton pratinjau. Mengubah resolusi, format, atau kecepatan bingkai akan memulai ulang pratinjau secara otomatis.

Open Camera menyediakan meja kerja lokal untuk mengonfigurasi dan menguji webcam. Versi 0.2.4 tidak memiliki perekaman, pemrosesan efek, atau keluaran kamera virtual.

<h2 id="roadmap">Peta jalan</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Fondasi kamera, validasi Linux, alat pengambilan, dan pengemasan AppImage, Debian, dan RPM">

| Panggung | Bekerja |
| --- | --- |
| **Tersedia · v0.2.4** | Pemilihan kamera, pratinjau langsung, sumber FPS, kontrol driver, diagnostik, dan tiga paket Linux. |
| **Berikutnya · Perangkat keras dan keandalan** | Validasi USB dan kamera internal, periksa 60+ mode FPS yang diiklankan pada perangkat keras, dan uji pemulihan saat perangkat sedang sibuk atau dicabut. |
| **Direncanakan · Tangkap alur kerja** | Tambahkan pengambilan foto dan video, overlay dan efek, lalu jelajahi profil dan keluaran kamera virtual. |

Peta jalan menetapkan prioritas tanpa tanggal target.

<h2 id="run-on-linux">📦 Jalankan di Linux</h2>

Unduh Open Camera **v0.2.4** dari [Rilis GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Unduh | Instal atau luncurkan |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` di Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` di Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` Kemudian `./OpenCamera-0.2.4-x86_64.AppImage` pada x86_64 Linux dengan glibc 2.39 atau lebih baru |

Mulai instalasi DEB atau RPM dari peluncur desktop atau dengan `open-camera`. Jika FUSE tidak tersedia, luncurkan AppImage dengan `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Untuk memeriksa unduhan, simpan [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) di samping paket dan jalankan `sha256sum -c --ignore-missing SHA256SUMS` dari direktori itu.

Alur kerja rilis menginstal atau meluncurkan ketiga paket dan memeriksa pratinjau langsung menggunakan sumber sintetis. Kompatibilitas webcam fisik masih memerlukan validasi.

### Jalankan dari sumber

Gunakan desktop Linux dengan Python 3.10 +, GTK 4.8 +, libadwaita 1.4 + dan GStreamer 1.20 +. Jalankan dari folder repositori dengan sistem Python sehingga dapat menemukan pengikatan PyGObject distribusi.

<details open>
<summary><b>Ubuntu 24.04 dan yang lebih baru</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>fedora</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Tes tanpa kamera fisik</b></summary>

```sh
python3 -m open_camera --test-source
```

Untuk penggunaan instalasi DEB atau RPM `open-camera --test-source`. Memilih **Pola pengujian GStreamer**, pilih 30, 60 atau 120 FPS pada 1280 × 720 dan klik **Mulai pratinjau**. Tarif ini menjelaskan sumber pengujian. Mode perangkat fisik bergantung pada kamera dan pengemudi.

</details>

### Pemecahan masalah

| Gejala | Apa yang harus diperiksa |
| --- | --- |
| Kameranya hilang | Hubungkan kembali, segarkan daftar perangkat dan periksa **Diagnostik** untuk komponen atau izin perangkat yang hilang. |
| Pratinjau gagal dimulai | Tutup aplikasi menggunakan kamera, coba **Otomatis**, lalu periksa **Diagnostik** untuk kesalahan pipa. Mode yang dikodekan mungkin memerlukan dekoder yang terpasang. |
| Sumber FPS berada di bawah tarif yang dipilih | Periksa tarif yang tersedia pada resolusi dan format tersebut. Coba resolusi yang lebih rendah atau port USB yang berbeda dan bandingkan ukurannya. |

Saat melaporkan masalah, sertakan distribusi, model kamera, mode pengambilan yang dipilih, dan teks yang relevan darinya **Diagnostik**.

<h2 id="design">Desain</h2>

Spanduk itu menunjukkan **prototipe browser interaktif**. Ini mencakup bingkai simulasi, efek, dan keluaran virtual sehingga antarmuka dapat dieksplorasi secara independen dari perangkat keras kamera. Unduh [prototipe HTML mandiri](design/open-camera-interface-options.html) dan buka di browser. Itu [lembar gaya tema](design/open-camera-themes.css) tersedia secara terpisah.

<details>
<summary><b>Pengembangan dan verifikasi</b></summary>

| Jalur | Tujuan |
| --- | --- |
| [open_camera/](open_camera/) | Antarmuka GTK, pratinjau GStreamer, dan kontrol V4L2 |
| [tes/](tests/) | Tes untuk parsing V4L2 dan validasi kontrol |
| [desain/](design/) | Prototipe interaktif, tema, ikon, dan tangkapan layar |
| [aset/readme/](assets/readme/) | Kartu README dan tombol navigasi |

```sh
python3 -m unittest discover -s tests -v
```

Pada desktop Linux, verifikasi mulai dan berhenti dengan pola pengujian pada 30 dan 60 FPS . Dengan kamera fisik, periksa mode yang diiklankan, kecepatan terukur, perubahan pada kontrol pengemudi, dan perilaku pemutusan sambungan.

Untuk membuat ulang panel README, instal Pillow di lingkungan pengembangan Anda dan jalankan:

```sh
python3 tools/build_readme_assets.py
```

</details>

## Tentang penulis

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx di GitHub"></a>

**sailxx** adalah pencipta Open Camera dan [Tobi](https://github.com/sailxx/Tobi), proyek yang menginspirasi gaya visual README ini. Proyek lain tersedia di [profil GitHub](https://github.com/sailxx).

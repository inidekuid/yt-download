# Mustika Downloader - YT-DLP Web Version

Mustika Downloader adalah aplikasi berbasis web sederhana namun kuat untuk mengunduh video atau audio dari YouTube. Aplikasi ini menggunakan pustaka `yt-dlp` untuk pemrosesan video dan `Flask-SocketIO` untuk memberikan laporan progres pengunduhan secara real-time kepada pengguna.

## Fitur Utama

- **Cek Info Video**: Menampilkan judul dan pilihan kualitas sebelum mengunduh.
- **Pilihan Kualitas**: Mendukung berbagai resolusi dari yang terendah hingga tertinggi (tergantung ketersediaan pada sumber).
- **Konversi MP3**: Mengonversi video ke format audio MP3 (192kbps) secara otomatis menggunakan FFmpeg.
- **Progress Bar Real-Time**: Visualisasi proses pengunduhan menggunakan Socket.IO.
- **Auto-Cleanup**: Menghapus file di server secara otomatis segera setelah pengguna selesai mengunduh file ke perangkat mereka.
- **Antarmuka Responsif**: Didesain dengan Bootstrap agar nyaman digunakan di PC maupun Smartphone.

## Prasyarat (Requirements)

Sebelum menjalankan aplikasi, pastikan sistem Anda telah terinstal:

- **Python 3.x**
- **FFmpeg**: Wajib terinstal dan terdaftar di _System Path_ untuk proses penggabungan video/audio dan konversi MP3.
- **yt-dlp**: Pustaka utama pengunduh.

## Instalasi

1.  **Clone atau Download repositori ini.**
2.  **Buat Virtual Environment (Disarankan kalau linux wajib ya, tapi untuk windows optional):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3.  **Instal Library yang dibutuhkan:**
    ```bash
    pip install flask flask-socketio yt-dlp
    ```

## Cara Menjalankan

1.  Pastikan Anda berada di direktori proyek.
2.  Jalankan aplikasi dengan perintah:
    ```bash
    python app.py
    ```
3.  Buka browser dan akses:
    `http://127.0.0.1:5000`

## Struktur Folder

```text
.
├── app.py              # Logika Backend (Flask & yt-dlp)
├── downloads/          # Folder sementara penyimpanan file
├── templates/
│   └── index.html      # Antarmuka Pengguna (Frontend)
└── README.md           # Dokumentasi proyek

> untuk file `ydownmp3.py` dan `ytdown2.py` ini versi CLI
```

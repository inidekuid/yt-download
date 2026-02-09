import yt_dlp
import os

def download_mp3(url, output_dir="downloads"):
    # Memastikan direktori output ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        # Mengambil audio terbaik
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(playlist_index)s_%(title)s.%(ext)s'),
        'nopart': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # Post-processors untuk konversi ke MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', # Kualitas bitrate (192kbps adalah standar yang bagus)
        }],
    }

    try:
        print(f"Sedang memproses unduhan ke: {output_dir}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nUnduhan selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("--- YouTube to MP3 Downloader ---")
    url = input("Masukkan URL video atau playlist: ")
    output_dir = input("Masukkan direktori output (default: downloads): ") or "downloads"
    download_mp3(url, output_dir)
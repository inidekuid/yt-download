import yt_dlp
import os

def download_video(url, output_dir="downloads"):
    # Memastikan direktori output ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        # 'bestvideo[height<=480]+bestaudio/best[height<=480]' lebih fleksibel dibanding hardcode '134'
        'format': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best',
        'outtmpl': os.path.join(output_dir, '%(playlist_index)s_%(title)s.%(ext)s'),
        # Menghapus 'quiet' agar kita bisa melihat jika ada error koneksi
        'nopart': True,
        # Menggunakan cookie atau user-agent seringkali membantu masalah "Remote end closed connection"
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Menggunakan download=True langsung lebih efisien untuk playlist maupun single video
            ydl.download([url])
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("--- YouTube Downloader (Fixed Version) ---")
    url = input("Masukkan URL video atau playlist: ")
    output_dir = input("Masukkan direktori output (default: downloads): ") or "downloads"
    download_video(url, output_dir)
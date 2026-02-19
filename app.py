from flask import Flask, render_template, request, jsonify, send_from_directory, send_file
from flask_socketio import SocketIO, emit
import yt_dlp
import os
import uuid

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Fungsi callback untuk yt-dlp
def progress_hook(d):
    if d['status'] == 'downloading':
        # Menghitung persentase
        p = d.get('_percent_str', '0%').replace('%','')
        socketio.emit('download_progress', {'percentage': p})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():
    url = request.json.get('url')
    ydl_opts = {'quiet': True, 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            formats = [
                {'format_id': f['format_id'], 'resolution': f'{f["height"]}p', 'ext': f['ext']}
                for f in info.get('formats', []) if f.get('vcodec') != 'none' and f.get('height')
            ]
            unique_formats = list({v['resolution']: v for v in formats}.values())
            return jsonify({'title': info['title'], 'formats': unique_formats})
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    format_id = data.get('format_id')
    mode = data.get('mode')

    unique_name = f"{uuid.uuid4().hex}"
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/{unique_name}.%(ext)s',
        'progress_hooks': [progress_hook], # Hubungkan ke fungsi progres
    }

    if mode == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
        })
    else:
        ydl_opts.update({'format': f'{format_id}+bestaudio/best', 'merge_output_format': 'mp4'})

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_ext = 'mp3' if mode == 'mp3' else 'mp4'
            filename = f"{unique_name}.{file_ext}"
            return jsonify({'file_url': f'/get_file/{filename}', 'title': info['title']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_file/<filename>')
def get_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    def generate():
        with open(file_path, 'rb') as f:
            yield from f
        # menghapus file setelah pengguna download selesai
        try:
            os.remove(file_path)
        except exception as e:
            print(f"Gagal Hapus File: {e}")
    #fungsi lama langsung download tidak hapus file di folder download
    #return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    return aa.response_class(
        generate(),
        mimetype='aplication/octet-stream',
        header={'Conten-Disposition': f'attachment; filename={filename}'}
    )

if __name__ == '__main__':
    socketio.run(app, debug=True)
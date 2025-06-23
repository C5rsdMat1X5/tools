import yt_dlp
def descargar_video(url, carpeta_destino='.'):
    opciones = {
        'outtmpl': f"{carpeta_destino}/%(title)s.%(ext)s",
        'format': 'best'
    }
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
url_video = input("Send the URL: ")
carpeta_destino = "/Users/matiashenriquez/YouTube"
descargar_video(url_video, carpeta_destino)
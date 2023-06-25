import pytube

def get_video_title(video_link):
    return pytube.YouTube(video_link).streams.get_highest_resolution().title
def get_youtube_video(video_link, quality, video_personal_ID):
    path_to_download = './app/static/app/videos'
    try:
        yt = pytube.YouTube(video_link)
        yt.streams.get_by_resolution(quality).download(output_path=path_to_download, filename=f"{video_personal_ID}.mp4")
        print("Видео скачалось")
    except Exception as exception:
        print(f"Ошибка! {exception}")

def get_video_quality(video_link):
    info = pytube.YouTube(video_link).streams.get_highest_resolution()
    return str(info.resolution)
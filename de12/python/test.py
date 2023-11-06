from pytube import YouTube

# YouTubeの動画URLを指定
url = 'https://www.youtube.com/watch?v=IVbY5edMfCA'

# YouTubeオブジェクトを作成
yt = YouTube(url)

# 音声ストリームを選択（ビデオではなく音声のみ）
stream = yt.streams.filter(only_audio=True).first()

# 音声を指定のフォルダにダウンロード
output_folder = 'C:/Users/suzyt/OneDrive/music'  # バックスラッシュまたは正斜線を使用
stream.download(output_path=output_folder)

print('音声をダウンロードしました。')

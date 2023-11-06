from pydub import AudioSegment

# MP4ファイルのパス
# mp4_file = "C:/Users/suzyt/OneDrive/music/CinderellaBoy.mp4"  # 正しいファイル名を指定
mp4_file = "C:/Users/suzyt/mygit/xbp/de12/python/CinderellaBoy.mp4"

# WAVファイルのパス（出力先）
# output_wav_file = 'C:/Users/suzyt/OneDrive/music/'  # 正しいファイル名を指定
output_wav_file = 'C:/Users/suzyt/mygit/xbp/de12/python/aaa'  # 正しいファイル名を指定

# MP4ファイルをWAVに変換
audio = AudioSegment.from_file(mp4_file, format="mp4")
audio.export(output_wav_file, format="wav")

print('MP4ファイルをWAVに変換しました。')

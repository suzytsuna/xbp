import librosa
import numpy as np
import soundfile as sf

# 音声ファイルを読み込む
audio_file = 'xbp/de12/python/aaa.wav'  # あなたがダウンロードした音声ファイルへのパス
y, sr = librosa.load(audio_file)

# 主旋律を抽出
melody, _ = librosa.effects.pitches(y=y, sr=sr)
melody = np.nan_to_num(melody)  # NaNを0に置き換える

# 主旋律を保存
output_file = '主旋律.wav'
sf.write(output_file, melody, sr)

print('主旋律を抽出し、保存しました。')

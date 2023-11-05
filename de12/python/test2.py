import librosa
import numpy as np
import soundfile as sf

# WAVファイルのパス
wav_file = 'xbp/de12/python/aaa.wav'  # 正しいファイル名を指定

# 音声ファイルを読み込む
y, sr = librosa.load(wav_file)

# 主旋律を抽出
melody, _ = librosa.piptrack(y=y, sr=sr)
melody = np.nan_to_num(melody)  # NaNを0に置き換える

# 主旋律を保存
output_file = 'C:/Users/suzyt/mygit/xbp/de12/python/aaa.wav'
sf.write(output_file, melody, sr)

print('主旋律を抽出し、保存しました。')

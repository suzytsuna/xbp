import librosa
import soundfile as sf

def change_key(input_file, output_file, target_key):
    # 音声ファイルを読み込む
    y, sr = librosa.load(input_file)

    # ターゲットのキーに変更する
    y_changed = librosa.effects.pitch_shift(y, sr, n_steps=get_pitch_shift_steps(target_key))

    # 新しい音声ファイルを保存する
    sf.write(output_file, y_changed, sr)

def get_pitch_shift_steps(target_key):
    # ターゲットのキーから変更する半音数を計算する
    # 例: Cメジャースケールからの変更を考慮しています
    key_map = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
        'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
    }

    target_key = target_key.upper()
    if target_key not in key_map:
        raise ValueError("Invalid target key")

    target_key_value = key_map[target_key]
    return target_key_value * +3  # 負の値で下げ、正の値で上げます

# 使用例
input_file = '"C:/Users/suzyt/Downloads./ADWIMPS - 愛にできることはまだあるかい [Official Music Video].wav"'  # 元の音声ファイル
output_file = 'aaa.wav'  # 新しいキーの音声ファイル
target_key = 'D'  # ターゲットのキー

change_key(input_file, output_file, target_key)

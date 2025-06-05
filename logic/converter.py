# logic/converter.py
from pathlib import Path
from ncmdump import NeteaseCloudMusicFile


def convert_multiple(files):
    results = []
    for file in files:
        input_path = Path(file)
        output_path = input_path.with_suffix(".mp3")
        try:
            ncm = NeteaseCloudMusicFile(input_path)
            ncm.decrypt()
            ncm.dump_music(output_path)
            results.append(f"{input_path.name} -> 成功")
        except Exception as e:
            results.append(f"{input_path.name} -> 失败: {e}")
    return results

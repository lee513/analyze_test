import glob
import pandas as pd

def load_subtitles_dataset(dataset_path):
    subtitle_paths = glob.glob(dataset_path + '/*.ass')

    scripts = []
    episode_num = []
    for path in subtitle_paths:

        with open(path, 'r') as file:
            lines = file.readlines()
            lines = lines[27:]
            lines = [','.join(line.split(',')[9:]) for line in lines]

        lines = [line.replace('\\N', ' ') for line in lines]
        script = " ".join(lines)

        episode = int(path.split('-')[-1].split('.')[0].strip())

        scripts.append(script)
        episode_num.append(episode)

    return pd.DataFrame.from_dict({"episode": episode_num, "script": scripts})

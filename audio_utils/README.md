# Anger Detection in Speech

* Audio, .csv files, venv for PyCharm and openSMILE could be downloaded from Google Drive: https://drive.google.com/open?id=1aKePojoILkyVTnx-SC_GMAgmBzTZRONb
* Unrar each archive in the root folder of the project.

# Rars:
* audio_features.rar - extracted features
* Audio_ang.rar - audio data for anger emotion
* Audio_neut.rar - audio data for neutral emotion
* Audio.rar - original dataset
* openSMILE-2.1.0.rar - installed openSMILE
* venv.rar - venv for PyCharm

# Folders:
.idea - folder with settings for PyCharm

# Files:
* arfftocsv.py - converter (from .arff format to .csv format)
* data_%s.csv, % some_emotion - annotation of the dataset
* debug_info.py - ffmpeg log
* extract_emotions.py - extract some_emotion audio from the dataset
* extract_features.py - extract features from some_emotion audio
* smile.log - openSMILE log

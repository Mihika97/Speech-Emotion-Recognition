import librosa
import numpy as np
import pandas as pd


def extract_feature(file_name, **kwargs):
    """
       Extract feature from audio file `file_name`
           Features supported:
               - MFCC (mfcc)
               - Chroma (chroma)
               - MEL Spectrogram Frequency (mel)
               - Contrast (contrast)
           e.g:
           `features = extract_feature(path, mel=True, mfcc=True)`
       """
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")

    df = pd.DataFrame(columns=["mfcc", "chroma", "mel", "contrast"])
    flag = 0

    for index, y in enumerate(file_name):
        X, sr = librosa.load(y, res_type='kaiser_fast', duration=3)
        sr = np.array(sr)
        st_ft = np.abs(librosa.stft(X))
        mfcc = np.mean(librosa.feature.mfcc(y=X, sr=sr, n_mfcc=40).T, axis=0)
        chroma = np.mean(librosa.feature.chroma_stft(S=st_ft, sr=sr).T, axis=0)
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sr).T, axis=0)
        contrast = np.mean(librosa.feature.spectral_contrast(S=st_ft, sr=sr).T, axis=0)
        df.loc[flag] = [mfcc, chroma, mel, contrast]
        flag = flag + 1

    return df





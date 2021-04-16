
import os
from keras.models import load_model

from numpy import loadtxt
from keras.models import load_model
import pandas as pd
import numpy as np
from keras.utils import to_categorical, np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder

import get_data
import feature_extract

List = get_data.get_data('clipped_files_new')

df = feature_extract.extract_feature(List, mfcc=True, chroma=True, mel=True, contrast=True)

mfcc_df = pd.DataFrame(df['mfcc'].values.tolist())
chroma_df = pd.DataFrame(df['chroma'].values.tolist())
mel_df = pd.DataFrame(df['mel'].values.tolist())
contrast_df = pd.DataFrame(df['contrast'].values.tolist())

df_cleaned = pd.concat([mfcc_df, chroma_df, mel_df, contrast_df], axis=1).reindex(mfcc_df.index)


X = df_cleaned
X_exp = np.expand_dims(X, axis=2)


# load model
model = load_model('/home/ml_new/storage_folder/saved_models/Initial_pitch_analysis.h5')

# summarize model.
# model.summary()

# evaluate the model
score = model.predict(X_exp, verbose=0)

score1 = pd.DataFrame(score)


le = LabelEncoder()
le.classes_ = np.load('/home/ml_new/storage_folder/label_classes.npy', allow_pickle=True)

pred_mod = score.argmax(axis=1)
pred_flat = pred_mod.astype(int).flatten()
pred_transformed = (le.inverse_transform(pred_flat))
pred_df = pd.DataFrame({'predicted_values': pred_transformed})

pred_df.to_csv('/home/ml_new/storage_folder/emotions.csv')

import numpy as np
import pandas as pd
import os

import librosa
import librosa.display
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import keras
import tensorflow as tf
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, Conv1D, Conv2D, MaxPooling1D, AveragePooling1D, BatchNormalization, \
    Input, Flatten, Dropout, Activation
from keras.utils import to_categorical, np_utils

import feature_extract
import get_data
import label_fetch
import model

List = get_data.get_data('data_combined')

df = feature_extract.extract_feature(List, mfcc=True, chroma=True, mel=True, contrast=True)

emotions = pd.DataFrame(columns=['emotion'])
flag = 0
for index, y in enumerate(List):
    emotion = label_fetch.get_emotion(y)
    emotions.loc[flag] = [emotion]
    flag = flag+1

mfcc_df = pd.DataFrame(df['mfcc'].values.tolist())
chroma_df = pd.DataFrame(df['chroma'].values.tolist())
mel_df = pd.DataFrame(df['mel'].values.tolist())
contrast_df = pd.DataFrame(df['contrast'].values.tolist())

df_cleaned = pd.concat([mfcc_df, chroma_df, mel_df, contrast_df, emotions['emotion']], axis=1).reindex(mfcc_df.index)

df_cleaned = df_cleaned.dropna(0)
shuffled_df = df_cleaned.sample(frac=1).reset_index(drop=True)
shuffled_df = shuffled_df.loc[~shuffled_df['emotion'].isin(['low_neutral', 'low_disgusted', 'low_surprised',
                                                            'shrill_neutral', 'shrill_disgusted', 'shrill_surprised'])]
X_train, X_test, y_train, y_test = train_test_split(shuffled_df.drop('emotion', axis=1), shuffled_df['emotion'],
                                                    test_size=0.2, random_state=0, shuffle=True)


# Transforming the textual labels into numerical categorical classes
lb = LabelEncoder()
y_train = np_utils.to_categorical(lb.fit_transform(y_train))
y_test = np_utils.to_categorical(lb.fit_transform(y_test))
np.save('/home/ml_new/storage_folder/label_classes.npy', lb.classes_)


# expanding dimensions for modelling
x_train_exp = np.expand_dims(X_train, axis=2)
x_test_exp = np.expand_dims(X_test, axis=2)


model, opt = model.ml_model()

# compiling the model
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])


# running the model
history = model.fit(x_train_exp, y_train, batch_size=256, epochs=1500, validation_data=(x_test_exp, y_test))

# displaying the model accuracy
train_result = model.evaluate(x_train_exp, y_train, verbose=0)
test_result = model.evaluate(x_test_exp, y_test, verbose=0)

print("train acc", "%s: %.2f%%" % (model.metrics_names[1], train_result[1]*100))
print("test acc", "%s: %.2f%%" % (model.metrics_names[1], test_result[1]*100))

# predicting the emotion labels over test set
pred = model.predict(x_test_exp, batch_size=512, verbose=1)
pred_mod = pred.argmax(axis=1)
pred_flat = pred_mod.astype(int).flatten()
pred_transformed = (lb.inverse_transform(pred_flat))
pred_df = pd.DataFrame({'predicted_values': pred_transformed})
actual_values = y_test.argmax(axis=1)
actual_values_mod = actual_values.astype(int).flatten()
actual_values_mod_transformed = (lb.inverse_transform(actual_values_mod))
actual_df = pd.DataFrame({'actual_values': actual_values_mod_transformed})
final_df = actual_df.join(pred_df)

# saving final model to be used on any audio file to predict emotions

model_name = 'Initial_pitch_analysis.h5'
save_dir = os.path.join('/home/ml_new/storage_folder', 'saved_models')
# Save model and weights

if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s' % model_path)

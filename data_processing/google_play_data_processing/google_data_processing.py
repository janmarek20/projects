# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df = pd.read_csv('./google_play_data_processing/googleplaystore.csv')

# %% preprocessing
df.info()

df.columns = [col.replace(' ', '_') for col in df.columns]

df = df.drop(10472)
df = df.reset_index()

df.Reviews = pd.to_numeric(df.Reviews)
# %% categories frequency
category_freq = df.groupby('Category').size().rename('Count')
category_freq.plot(kind='bar', color='green', alpha=0.5, title='Categories')

# %% type frequency
type_freq = df.groupby('Type').size().rename('Count')
type_freq.plot(kind='pie', fontsize=16)

# %%
df_part = df[['Genres', 'Rating', 'Type']]
temp = df_part.groupby(['Genres', 'Type']).agg({'Rating': ['count', 'mean']})
temp.columns = ['_'.join(x) for x in temp.columns.ravel()]

temp = temp.sort_values('Rating_count', ascending=False)
temp_mask = temp[temp['Rating_count'] > 100]
temp_mask.plot(kind='bar', subplots=True)

# %% top 5 high rating product
top_5 = temp.nlargest(5, columns='Rating_count')['Rating_count']
top_5.plot(kind='pie')
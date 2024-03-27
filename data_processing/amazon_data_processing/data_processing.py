# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# %% import data
df = pd.read_csv('./amazon_data_processing/Consumer_Reviews_Amazon.csv', index_col=0)

# %%
df.describe()

# %%
for col in df.columns:
    print(col)
    
df.columns = [col.replace('.', '_') for col in df.columns]

# %%
df = df[['name', 'primaryCategories', 'reviews_rating', 'reviews_text']]

# %%
df.columns = ['name', 'category', 'rating', 'text']
df.info()
df.describe()

# %% export
df.to_csv('./amazon_data_processing/amazon_reviews_clean.csv')


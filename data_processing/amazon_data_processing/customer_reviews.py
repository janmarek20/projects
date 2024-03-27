# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import seaborn as sns
sns.set()


# %% import data
df = df = pd.read_csv('./amazon_data_processing/amazon_reviews_clean.csv',
                      index_col=0)

# %% plotting categories
df['category'].value_counts().plot(kind='pie')

# %% plotting ratings frequency
df['rating'].value_counts().sort_index().plot(kind='bar', legend=True,
                                              title='Frequency')

# %% extract top 3 most rating products
top_3 = df.groupby('name').count()['rating'].rename('count').nlargest(3)
top_3.plot(kind='bar')

# %% extract top 3 high rating product
top_3_rat = df.groupby('name').aggregate('mean').sort_values('rating',
                            ascending=False).nlargest(3, columns='rating')

# %% extract bottom 3 product
bottom_3_ra = df.groupby('name').aggregate('mean')['rating'].\
    sort_values().nsmallest(3)
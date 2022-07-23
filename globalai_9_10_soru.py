# -*- coding: utf-8 -*-
"""globalai_9-10.soru.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OoWf8ANaEhFfdEYkaX7az2XN1vEbMUcR

# Kütüphaneler
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""# Verisetini Yükleme"""

data = pd.read_csv("NetflixOriginals.csv",encoding="ISO-8859-1")

data.head()

"""# IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.

"""

df=data.groupby("Genre").agg({"IMDB Score": "max"}).sort_values(by="IMDB Score", ascending=False)[0:10]
genre = df.reset_index()
sns.barplot(y=genre["Genre"], x=genre["IMDB Score"])
plt.show()

"""# 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz."""

df=data.groupby("Title").agg({"Runtime": "max"}).sort_values(by="Runtime", ascending=False)[0:10]
runtime = df.reset_index()
fig, ax = plt.subplots(figsize=(25,7),dpi=100)
ax.scatter(y=runtime["Runtime"], x=runtime["Title"], s=75, color='darkred', alpha=0.7)
sns.lineplot(x=runtime["Title"], y=runtime["Runtime"])
plt.show()
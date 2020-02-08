# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import PreprocessText
import EntropyCount

import numpy as np
from sklearn.linear_model import LinearRegression


import pandas as pd
import matplotlib.pyplot as plt


# +
# Preprocesing i liczenie entropi dla naszego dziennika

# +
# def preprocess_paper(dir_, articles_amount, paper_name):
    
#     list_articles = []
    
#     for n in range(articles_amount):
#         file = str(n) + ".txt"

#         prep = PreprocessText.whole_proces_polish(dir_, file)
#         entropy, amount_tokens = EntropyCount.calculate_entropy_for_all_words(prep)

#         list_this = []
#         list_this.append(n)
#         list_this.append(paper_name)
#         list_this.append(prep[:3])
#         list_this.append(amount_tokens)
#         list_this.append(entropy)
        
#         list_articles.append(list_this)
    
#     return list_articles
# -
def whole_preprocess_entrpy_entrate(dir_, articles_amount, paper_name):
    list_articles = []

    for n in range(articles_amount):
        file = str(n) + ".txt"

        prep = PreprocessText.preprocess_article(dir_, file)
        entropy, amount_tokens = EntropyCount.calculate_entropy_for_all_words(prep)
        entropy_rate = EntropyCount.entropy_rate_calculate(prep)

        list_this = []
        list_this.append(n)
        list_this.append(paper_name)
        list_this.append(prep[:3])
        list_this.append(amount_tokens)
        list_this.append(entropy)
        list_this.append(entropy_rate)

        list_articles.append(list_this)
        

    return list_articles




# +
dir_ = "teksty/nasz_dziennik/all_articles/"
paper_name = "Nasz Dziennik"
articles_amount = 52 #52

list_nasz = whole_preprocess_entrpy_entrate(dir_, articles_amount, paper_name)


# -

list_nasz[:5]

df_nasz = pd.DataFrame(list_nasz, columns = ["Numer artykułu", "Nazwa gazety", "Pierwsze lematy", "Ilość tokenów", "Entropia", "Wskaźnik entropii"])

df_nasz[:10]

# +
dir_ = "teksty/gazeta_wyborcza/all_articles/"
paper_name = "Gazeta Wyborcza"
articles_amount = 48 #48

list_gw = whole_preprocess_entrpy_entrate(dir_, articles_amount, paper_name)


# -

df_gw = pd.DataFrame(list_gw, columns = ["Numer artykułu", "Nazwa gazety", "Pierwsze lematy", "Ilość tokenów", "Entropia", "Wskaźnik entropii"])

df_gw[:10]

# +
# liczenie średniej entropi dla wszystkich artykułów w gazecie
# -

enntropy_mean_nd = df_nasz.loc[:,"Entropia"].mean()

enntropy_mean_gw = df_gw.loc[:,"Entropia"].mean()

# +
# liczenie średniego wskaźnika entropi dla wszystkich artykułów w gazecie
# -

enntropy_rate_mean_nd = df_nasz.loc[:,"Wskaźnik entropii"].mean()
enntropy_rate_mean_gw = df_gw.loc[:,"Wskaźnik entropii"].mean()



l_ent_nd = ["Nasz Dziennik", enntropy_mean_nd, enntropy_rate_mean_nd]
l_ent_gw = ["Gazeta Wyborcza", enntropy_mean_gw, enntropy_rate_mean_gw]
l_ent_mean = [l_ent_nd, l_ent_gw]

l_ent_mean

df_mean = pd.DataFrame(l_ent_mean, columns = ["Nazwa Gazety", "Średnia Entopia", "Wskaźnik entropii"])

df_mean

# +
fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

ax.table(cellText=df_mean.values, colLabels=df_mean.columns, loc='center')

fig.tight_layout()
plt.savefig('entropy_papers.png')
plt.show()

# +
# plt.plot(df_nasz.loc[:,"Ilość tokenów"], df_nasz.loc[:,"Entropia"])

# +
# p1, = host.plot(df_nasz.loc[:,"Ilość tokenów"], df_nasz.loc[:,"Entropia"], "b-", label="Nasz Dziennik")
# p2, = par1.plot(df_gw.loc[:,"Ilość tokenów"], df_gw.loc[:,"Entropia"], "b-", label="Gazeta Wyborcza")

# +
# plt.plot(df_nasz.loc[:,"Ilość tokenów"].sort_values(by=['Ilość tokenów'], df_nasz.loc[:,"Entropia"], 'r--', df_gw.loc[:,"Ilość tokenów"], df_gw.loc[:,"Entropia"], 'bs-')
# plt.show()

# +
# df_nasz.sort_values(by=['Ilość tokenów']).loc[:,"Ilość tokenów"]

# +
# df_nasz.sort_values(by=['Ilość tokenów']).loc[:,"Entropia"]

# +
# Sortowanie DF po ilości tokenów
# -

df_gw_tokens = df_gw.sort_values(by=['Ilość tokenów'])
df_gw_tokens[:10]

df_nd_tokens = df_nasz.sort_values(by=['Ilość tokenów'])
df_nd_tokens[:10]

# +
# df_gw_tokens["Entropia"]

# +
# Wykres, gdzie osią x jest ilość słów a osią y entropia
# niebieski to GW
# czerwony to ND
# -

plt.plot(df_nd_tokens.loc[:,"Ilość tokenów"], df_nd_tokens.loc[:,"Entropia"], 'r-', df_gw_tokens.loc[:,"Ilość tokenów"], df_gw_tokens.loc[:,"Entropia"], 'b-')
plt.title("Porównanie entropii(oś y) obu gazet w stosunku do ilości tokenów(oś x)", fontsize=12)
# fig.suptitle('This is a somewhat long figure title', fontsize=16)
plt.xlabel('Ilość Tokenów')
plt.ylabel('Entropia')
plt.savefig('tokens_entropy.png')
plt.legend(("Nasz dziennik", "Gazeta wyborcza"), loc='lower right')
plt.show()

plt.plot(df_nd_tokens.loc[:,"Ilość tokenów"], df_nd_tokens.loc[:,"Wskaźnik entropii"], 'm-', df_gw_tokens.loc[:,"Ilość tokenów"], df_gw_tokens.loc[:,"Wskaźnik entropii"], 'g-')
plt.title("Porównanie wzkaźnika entropii(y) obu gazet w stosunku do ilości tokenów(x)", fontsize=11)
# fig.suptitle('This is a somewhat long figure title', fontsize=16)
plt.xlabel('Ilość Tokenów')
plt.ylabel('Wskaźnik entropii')
plt.savefig('tokens_entropy_rate.png')
plt.legend(("Nasz dziennik", "Gazeta wyborcza"), loc='lower right')
plt.show()







# +
# plt.plot(df_nd_tokens.loc[:,"Entropia"], df_nd_tokens.loc[:,"Wskaźnik entropii"], 'ro')
plt.title("Regresja linowa wskaźnika entropii (y) względem entropii(x) dla Naszego Dziennika", fontsize=10)
# fig.suptitle('This is a somewhat long figure title', fontsize=16)
plt.xlabel('Entropia')
plt.ylabel('Wskaźnik entropii')

# plt.legend(("Entropia", "Wskaźnik entropii"), loc='lower right')
# plt.show()

X = df_nd_tokens["Entropia"].values.reshape(-1, 1)
Y = df_nd_tokens["Wskaźnik entropii"]
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')

plt.savefig('entropy_entrate_ND.png')
plt.show()
# -



# +
# plt.plot(df_nd_tokens.loc[:,"Entropia"], df_nd_tokens.loc[:,"Wskaźnik entropii"], 'ro')
plt.title("Regresja linowa wskaźnika entropii (y) względem entropii(x) dla Gazety Wyborczej", fontsize=11)
# fig.suptitle('This is a somewhat long figure title', fontsize=16)
plt.xlabel('Entropia')
plt.ylabel('Wskaźnik entropii')

# plt.legend(("Entropia", "Wskaźnik entropii"), loc='lower right')
# plt.show()

X = df_gw_tokens["Entropia"].values.reshape(-1, 1)
Y = df_gw_tokens["Wskaźnik entropii"]
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.savefig('entropy_entrate_GW.png')
plt.show()
# -











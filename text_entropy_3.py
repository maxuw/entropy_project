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



# +
dir_ = "teksty/nasz_dziennik/all_articles/"
paper_name = "Nasz Dziennik"
articles_amount = 52

list_nasz = PreprocessText.preprocess_paper(dir_, articles_amount, paper_name)


# -

list_nasz[:5]

df_nasz = pd.DataFrame(list_nasz, columns = ["Numer artykułu", "Nazwa gazety", "Pierwsze lematy", "Ilość tokenów", "Entropia"])

df_nasz[:10]

# +
dir_ = "teksty/gazeta_wyborcza/all_articles/"
paper_name = "Gazeta Wyborcza"
articles_amount = 48

list_gw = PreprocessText.preprocess_paper(dir_, articles_amount, paper_name)


# -

df_gw = pd.DataFrame(list_gw, columns = ["Numer artykułu", "Nazwa gazety", "Pierwsze lematy", "Ilość tokenów", "Entropia"])

df_gw[:10]

# +
enntropy_mean_nd = df_nasz.loc[:,"Entropia"].mean()

# list_en_mean_nd = pd.Series("", "", "", "", enntropy_mean_nd)

# df_nasz = df_nasz.append(list_en_mean_nd)
# -

df_nasz



enntropy_mean_gw = df_gw.loc[:,"Entropia"].mean()

l_ent_nd = ["Nasz Dziennik", enntropy_mean_nd]
l_ent_gw = ["Gazeta Wyborcza", enntropy_mean_gw]
l_ent_mean = [l_ent_nd, l_ent_gw]

l_ent_mean

df_mean = pd.DataFrame(l_ent_mean, columns = ["Nazwa Gazety", "Średnia Entopia"])

df_mean



plt.plot(df_nasz.loc[:,"Ilość tokenów"], df_nasz.loc[:,"Entropia"])

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
# -

df_gw_tokens = df_gw.sort_values(by=['Ilość tokenów'])
df_gw_tokens[:10]

df_nd_tokens = df_nasz.sort_values(by=['Ilość tokenów'])
df_nd_tokens[:10]

# +
# df_gw_tokens["Entropia"]
# -

plt.plot(df_nd_tokens.loc[:,"Ilość tokenów"], df_nd_tokens.loc[:,"Entropia"], 'r-', df_gw_tokens.loc[:,"Ilość tokenów"], df_gw_tokens.loc[:,"Entropia"], 'b-')
plt.xlabel('Ilość Tokenów')
plt.ylabel('Entropia')
plt.savefig('foo.png')
plt.show()



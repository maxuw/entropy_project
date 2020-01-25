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

dir = "teksty/nasz_dziennik/wirus/"

file = "1.txt"

process1 = PreprocessText.whole_proces_polish(dir, file)

process1[:20]



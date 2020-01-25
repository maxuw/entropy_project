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

file_1 = PreprocessText.read_files(file, dir)

file_1[:100]

processed_inner_text = PreprocessText.remove_empty_linesc(file_1)[2]

processed_inner_text

body1 = PreprocessText.join_lines(processed_inner_text)

body1

import string

body1.translate(str.maketrans('', '', string.punctuation))



body_nopunct = PreprocessText.remove_punctuation(body1)

body_nopunct

filename = PreprocessText.write_body_tofile(dir, file, body_nopunct)
filename

output = PreprocessText.run_udpipe(filename)
output[:200]





lemmas = PreprocessText.find_lemmas(output)
lemmas[:10]

process1 = PreprocessText.whole_proces_polish("teksty/gazeta_wyborcza/wirus/", file)

process1



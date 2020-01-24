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

from class_preporocess_text import PreprocessText

dir = "teksty/nasz_dziennik/wirus/"

file = "1.txt"

file_1 = PreprocessText.read_files(file, dir)

file_1[:100]

processed_inner_text = PreprocessText.process(file_1)[2]

processed_inner_text

body1 = PreprocessText.join_lines(processed_inner_text)

body1



filename = PreprocessText.write_body_tofile(dir, file, body1)
filename

output = PreprocessText.run_udpipe(filename)
output[:200]





lemmas = PreprocessText.find_lemmas(output)
lemmas[:10]

process1 = class_preporocess_text.whole_proces_polish(dir, file)

import class_preporocess_text

class_preporocess_text.dupa("bbb")



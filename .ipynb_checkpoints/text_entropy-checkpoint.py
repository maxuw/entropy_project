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

from class_preporocess_text import PreprocessText


import os
os.environ['PATH'] = os.environ['PATH'] + ':udpipe-1.2.0-bin/bin-linux64/'

dir = "teksty/nasz_dziennik/wirus/"

file = "1.txt"


def read_files(file_name, dir):

    f = open(dir + file_name, "r")
    text = f.read()

    return text


file_1 = read_files(file, dir)

file_1



def process(string):
    string = string.splitlines()
    
    new_string = []
    for s in string:
        if s != "":
            new_string.append(s)
            
    
    return new_string[0], new_string[1], new_string[2:]

processed_inner_text = process(file_1)[2]


def join_lines(string):
    
    string_long = ""
    for l in string:
        string_long = string_long + " " + l
        
    
    return string_long

processed_inner_text

body1 = join_lines(processed_inner_text)



# +
# # ! wget https://github.com/ufal/udpipe/releases/download/v1.2.0/udpipe-1.2.0-bin.zip
# # ! unzip udpipe-1.2.0-bin.zip
# # ! rm udpipe-1.2.0-bin.zip

# +
# # ! udpipe

# +
# # ! curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2898/polish-lfg-ud-2.3-181115.udpipe
# # ! curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2898/polish-sz-ud-2.3-181115.udpipe

# +
# # ! curl --remote-name https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2895/ud-treebanks-v2.3.tgz
# # ! tar zxf ud-treebanks-v2.3.tgz
# # ! rm ud-treebanks-v2.3.tgz
# -



# +
# zapisuję plik pod nową nazwą

def write_body_tofile(file_name, text):
    text_file = dir + file_name.split(".")[0] + "_body_cleaned.txt"

    with open(text_file, "w") as f:
        f.write(text)


# -

def run_udpipe(dir, file_name):
    stream = os.popen("udpipe --tag --input=horizontal polish-sz-ud-2.3-181115.udpipe " + dir + file_name)
    output = stream.read()
    return output


write_body_tofile(file, body1)

output = run_udpipe(dir, "1_body_cleaned.txt")
output


def find_lemmas(string):
    matches_lemmas_all = re.findall(r"n[0-9]+\\t(.*?)\\t[A-Z][A-Z]+", string)
    return matches_lemmas_all


matches_lemmas_all = re.findall(r"n[0-9]+\\t(.*?)\\t[A-Z][A-Z]+", output)


matches_lemmas_all = re.findall(r'[0-9]+\t.*?\t(.*?)\t[A-Z][A-Z]+', output)


n[0-9]+\\t.+?\\t(.+?)\\t[A-Z][A-Z]+

matches_lemmas_all

n[0-9]+\\t.+?\\t(.+?)\\t[A-Z][A-Z]+

  ## Suppose we have a text with many email addresses
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
  emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
  for email in emails:
    # do something with each found email string
    print(email)

import re

output





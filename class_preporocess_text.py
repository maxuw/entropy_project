import os
import re

os.environ['PATH'] = os.environ['PATH'] + ':udpipe-1.2.0-bin/bin-linux64/'


def read_files(file_name, dir):
    f = open(dir + file_name, "r")
    text = f.read()

    return text

def process(string):
    string = string.splitlines()

    new_string = []
    for s in string:
        if s != "":
            new_string.append(s)

    return new_string[0], new_string[1], new_string[2:]

def join_lines(string):

    string_long = ""
    for l in string:
        string_long = string_long + " " + l

    return string_long


def write_body_tofile(dir, file_name, text):
    print(file_name)
    print(file_name.split(".")[0])
    file_name_clean = dir + file_name.split(".")[0] + "_body_cleaned.txt"

    with open(file_name_clean, "w") as f:
        f.write(text)

    return file_name_clean


def run_udpipe(file_name):
    stream = os.popen("udpipe --tag --input=horizontal polish-sz-ud-2.3-181115.udpipe " + file_name)
    output = stream.read()
    # print(output)
    return output



def find_lemmas(string_):
    matches_lemmas_all = re.findall(r'[0-9]+\t.*?\t(.*?)\t[A-Z][A-Z]+', string_)
    return matches_lemmas_all

def whole_proces_polish(dir, filename):
    text_from_file = read_files(filename, dir)
    body_from_file = process(text_from_file)[2]
    joined_body = join_lines(body_from_file)
    new_filename = write_body_tofile(dir, filename, joined_body)
    udpipe_output = run_udpipe(new_filename)
    lemmas = find_lemmas(udpipe_output)
    return lemmas


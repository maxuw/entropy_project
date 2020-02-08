import os
import re
import string
import EntropyCount

os.environ['PATH'] = os.environ['PATH'] + ':udpipe-1.2.0-bin/bin-linux64/'


def read_files(file_name, dir, verbose=False):
    f = open(dir + file_name, "r")
    text = f.read()

    if verbose == True:
        print(text[:150])

    return text

def remove_empty_linesc(string, verbose=False):
    string = string.splitlines()

    new_string = []
    for s in string:
        if s != "":
            new_string.append(s)

    if verbose == True:
        print(new_string[2:][:10])

    return new_string[0], new_string[1], new_string[2:]

def join_lines(string_, verbose=False):

    string_long = ""
    for l in string_:
        string_long = string_long + " " + l

    if verbose == True:
        print(string_long[:200])

    return string_long

def remove_punctuation(string_, verbose=False):
    string_ = string_.translate(str.maketrans('', '', string.punctuation))
    string_ = string_.replace("–", " ")

    if verbose == True:
        print(string_[:200])

    return string_

def write_body_tofile(dir, file_name, text):
    # print(file_name)
    # print(file_name.split(".")[0])
    file_name_clean = dir + file_name.split(".")[0] + "_body_cleaned.txt"

    with open(file_name_clean, "w") as f:
        f.write(text)


    return file_name_clean


def run_udpipe(file_name, verbose=False):
    stream = os.popen("udpipe --tag --input=horizontal polish-sz-ud-2.3-181115.udpipe " + file_name)
    output = stream.read()
    # print(output)

    if verbose == True:
        print(output[:500])

    return output



def find_lemmas(string_, verbose=False):
    matches_lemmas_all = re.findall(r'[0-9]+\t.*?\t(.*?)\t[A-Z][A-Z]+', string_)
    if verbose == True:
        print(matches_lemmas_all[:20])
    return matches_lemmas_all

def preprocess_article(dir, filename, verbose=False):
    text_from_file = read_files(filename, dir, verbose)
    body_from_file = remove_empty_linesc(text_from_file, verbose)[2]
    joined_body = join_lines(body_from_file, verbose)
    body_without_punctuation = remove_punctuation(joined_body, verbose)
    new_filename = write_body_tofile(dir, filename, body_without_punctuation)

    udpipe_output = run_udpipe(new_filename, verbose)
    lemmas = find_lemmas(udpipe_output, verbose)
    return lemmas


# def preprocess_all articles(dir_, articles_amount, paper_name):
#     list_articles = []
#
#     for n in range(articles_amount):
#         file = str(n) + ".txt"
#
#         prep = whole_proces_polish(dir_, file)
#         entropy, amount_tokens = EntropyCount.calculate_entropy_for_all_words(prep)
#
#         list_this = []
#         list_this.append(n)
#         list_this.append(paper_name)
#         list_this.append(prep[:3])
#         list_this.append(amount_tokens)
#         list_this.append(entropy)
#
#         list_articles.append(list_this)
#
#     return list_articles
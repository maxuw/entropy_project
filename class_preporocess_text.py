import os
os.environ['PATH'] = os.environ['PATH'] + ':udpipe-1.2.0-bin/bin-linux64/'

class Preprocess_text:

    def read_files(self, file_name, dir):
        f = open(dir + file_name, "r")
        text = f.read()

        return text

    def process(self, string):
        string = string.splitlines()

        new_string = []
        for s in string:
            if s != "":
                new_string.append(s)

        return new_string[0], new_string[1], new_string[2:]

    def join_lines(self. string):

        string_long = ""
        for l in string:
            string_long = string_long + " " + l

        return string_long


    def write_body_tofile(self, file_name, text):
        text_file = dir + file_name.split(".")[0] + "_body_cleaned.txt"

        with open(text_file, "w") as f:
            f.write(text)


    def run_udpipe(self, dir, file_name):
        stream = os.popen("udpipe --tag --input=horizontal polish-sz-ud-2.3-181115.udpipe " + dir + file_name)
        output = stream.read()
        return output



    def find_lemmas(self, string):
        matches_lemmas_all = re.findall(r"n[0-9]+\\t(.*?)\\t[A-Z][A-Z]+", string)
        return matches_lemmas_all
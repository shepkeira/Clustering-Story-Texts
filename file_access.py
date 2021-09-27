import os
import re
# input: directory_path you want file from
# output: list of all files in a directory
def get_file_names(directory_path):
    files = os.listdir(directory_path)
    return files

# input: file name to get contents from
# output: all content of the docs into one string variable
def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f:
        file_contents = f.read()
        return file_contents

# input: file_name you want to read contents for
# output: the contents of a file in an array of sentences which are arrays of words
def read_processed_file(file_name):
    file_contents = []
    with open(file_name, 'r', encoding="utf8") as f:
        myline = f.readline()
        while myline:
            myline = re.sub('\n', '', myline)
            file_line_array = re.split(' ', myline)
            file_contents.append(file_line_array)
            myline = f.readline()
    return file_contents

# input: contents of a file; file_name you want to write to
# output: nothing
# this function writes contents of a proccessed file into a new file under "processed_docs"
def write_contents_to_file(contents, file_name):
    path = os.path.join(os.getcwd(), "processed_docs", file_name)
    f = open(path, 'w', encoding='utf8')
    f.write(contents)
    f.close()

# input: nothing
# output: a dictionary of file_names: processed text docs contents
def get_preprocessed_file_contents():
    processed_docs_path = os.path.join(os.getcwd(), "processed_docs")
    if os.path.exists(processed_docs_path):
        file_names = get_file_names(processed_docs_path)
        files_contents = {}
        for file_name in file_names:
            doc_path = os.path.join(processed_docs_path, file_name)
            files_contents[file_name] = read_file(doc_path)
        return files_contents
    else:
        print("There was an error.")
        return 0

# input: nothing
# output: dictionary of file_names: file_content_strings from the alldocs folder
def get_file_contents():
    docs_path = os.path.join(os.getcwd(), "alldocs")
    if os.path.exists(docs_path):
        file_names = get_file_names(docs_path)
        files_contents = {}
        for file_name in file_names:
            doc_path = os.path.join(docs_path, file_name)
            files_contents[file_name] = read_file(doc_path)
        return files_contents
    else:
        print("Files not found.")
        return 0

def write_matrix_to_file(table):
    # file_contents = ""
    # for file_name, metrics in table.items():
    #     file_contents += file_name + ": " + (' ').join(map(str, metrics)) + "\n"
    path = os.path.join(os.getcwd(), "matrix", "cosine_matrix")
    f = open(path, 'w')
    f.write(table)
    f.close()
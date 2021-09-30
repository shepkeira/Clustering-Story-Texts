import re
import math
from heapq import nlargest

# input: list of terms to caluclate dv for; doucmetn to caluclate dv for; documents including doument considered
# output: doucment vector (list)
def document_vector(terms, document, documents):
    d_vector = []
    doc_array = re.split(" ", document)
    document_dict = all_terms_frequency(doc_array)
    for term in terms:
        tfidf = term_frequency_inverse_document_frequency(term, document_dict, documents)
        d_vector.append(tfidf)
    return d_vector

# input: a dictionary of file_names: docuements
# output: a list of all the terms in the doucments (no duplicates)
def all_terms(documents):
    terms = []
    for _name, doc in documents.items():
        document_array = re.split(" ", doc)
        file_term_frequency_dict = all_terms_frequency(document_array)
        all_terms_in_doc = list(file_term_frequency_dict.keys())
        for term in all_terms_in_doc:
            if term not in terms:
                terms.append(term)
    return terms

# tfidf(t, d, D) = tf(t,d) * idf(t,D)
# input: string of term; dictionary of document term frequencies; documents in a dictionary
# output: term frequency * inverse_document_freqncy for that term and document
def term_frequency_inverse_document_frequency(term, document_dict, documents):
    tf = term_frequency(term, document_dict)
    # print(type(tf))
    idf = inverse_document_frequency(term, documents)
    # print(type(idf))
    return tf*idf

#idf(t, D) = log( |D| / df(t,D))
# input: string of term; dictionary of documents
# output: log of (# of docuemnets / documetn_frequency of term); if document_frequency of term is 0, log is log(1)
def inverse_document_frequency(term, documents):
    df = document_frequency(term, documents)
    number_of_docuemts = len(documents)
    if df == 0:
        return math.log(1)
    return math.log(number_of_docuemts/df)

# df(t,D) docuements frequency # of doucments that contain t
# input: string of term to find docuement freq for; dictionary of doucments
# output: number of times that term appears in all documents
def document_frequency(term, docuements):
    frequency_of_term = 0
    for _file_name, document in docuements.items():
        if term in document:
            frequency_of_term += 1
    return frequency_of_term

# tf(t,d) = frequency of t in d / total number of terms in d
#Input: term to find term frequency for; dictionary of term frequencies
#Output: 0 if term is not in document, or if document_dict is empty; else frequnency of term / # of terms
def term_frequency(term, document_dict):
    total_number_of_terms = len(document_dict)
    frequency_of_term = 0
    if term in document_dict:
        frequency_of_term = document_dict[term]
    if total_number_of_terms != 0:
        return frequency_of_term/total_number_of_terms
    return 0

#input: array of document words
#output: dict of terms and freqs.
def all_terms_frequency(document_array):
    term_freq_dict = {}
    for term in document_array:
        if term in term_freq_dict:
            term_freq_dict[term] += 1
        else:
            term_freq_dict[term] = 1
    return term_freq_dict
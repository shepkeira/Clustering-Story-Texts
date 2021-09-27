from file_access import *
from pre_processing import process_contents
from document_vectors import document_vector, top_10_percent_terms, all_terms
from document_similarity import cosine_matrix
from tabulate import tabulate
# an example of preprocessed text file (matching the required one)
# a nicely displaed NxN matrix of cosine similarity
# your cluster analysis results (membership and dendrogram)

## Applying Clustering
# 1) Apply agglomerative hierarchical clustering on the set of doucments using MIN (ie signle linkage) as your proximity measure of similarity beween two clusters
#    If you are using a package to call this algorithm, then return the dendrogram in your result
#    Corresponding to that result, identify the set of documents (by file name) that are in each of your cluters for k=2

#    If you implemetn the above clustering algorithmm on your own then display the items in each of your clusters (by file name) for k=2

def main():
    # Read in data
    files_contents = get_file_contents()
    if files_contents == 0:
        print("There was an error. Please confirm that the files are located in /alldocs.")
    # Process files
    for file_name, file_contents in files_contents.items():
        # Process Your Files
        preprocessed_contents = process_contents(file_contents)
        # Write file contents to preprocessed_docs
        write_contents_to_file(preprocessed_contents, file_name)
    preprocessed_files = get_preprocessed_file_contents()
    if preprocessed_files == 0:
        print("There was an error. Please confirm that the files are located in /processed_docs")
    # Creating Document Vectors
    # get top 10% terms from each file (no dups)
    terms = all_terms(preprocessed_files)#top_10_percent_terms(preprocessed_files)
    document_vectors = {}
    for file_name, file_contents in preprocessed_files.items():
        # calulate docuement vector for terms for each file
        dv = document_vector(terms, file_contents, preprocessed_files)
        document_vectors[file_name] = dv
    # Computing Document Similarity
    cosine_matrix_n_x_n = cosine_matrix(document_vectors)
    table = tabulate(cosine_matrix_n_x_n)
    write_matrix_to_file(table)

# runs main to start
if __name__ == "__main__":
    main()
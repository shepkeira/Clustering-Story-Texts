from file_access import *
from pre_processing import process_contents
from document_vectors import document_vector, all_terms
from document_similarity import cosine_matrix
from tabulate import tabulate
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc

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
    cosine_matrix_n_x_n, file_names = cosine_matrix(document_vectors)
    table = tabulate(cosine_matrix_n_x_n)
    write_matrix_to_file(table)
    df_matrix = pd.DataFrame(cosine_matrix_n_x_n, columns= file_names)
    # Cluster Based on Cosine Matrix
    model = AgglomerativeClustering(n_clusters=2, affinity='cosine', linkage='single')
    model.fit_predict(df_matrix)
    # Split the Clusters
    labels = model.labels_
    cluster_a_indexes = [i for i in range(len(labels)) if labels[i] == 0]
    cluster_a_column_names = []
    for column_index in cluster_a_indexes:
        cluster_a_column_names.append(file_names[column_index])
    cluster_b_indexes = [i for i in range(len(labels)) if labels[i] == 1]
    cluster_b_column_names = []
    for column_index in cluster_b_indexes:
        cluster_b_column_names.append(file_names[column_index])
    cluster_a = "In cluster A there is: " + ', '.join(cluster_a_column_names)
    cluster_b = "In cluster B there is: " + ', '.join(cluster_b_column_names)
    # Write clusters to file
    write_clusters_to_file(cluster_a, cluster_b)
    # Create dendogram
    shc.dendrogram((shc.linkage(df_matrix, method ='single')), labels=file_names, color_threshold=0.8, above_threshold_color="green")
    # Save dendogram as image
    path = os.path.join(os.getcwd(), "results", "dendogram.png")
    plt.savefig(path)

# runs main to start
if __name__ == "__main__":
    main()
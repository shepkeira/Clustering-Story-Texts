from document_vectors import document_vector
import math
## Computing Document Similarity
# 1) For each pair of doucments, compute their cosine similarity, and store the results in an NxN matrix (where N= # documents here 28)

def cosine_matrix(document_vectors):
    matrix = []
    file_names = []
    for name_i, document_vector_i in document_vectors.items():
        matrix_row_i = []
        file_names.append(name_i)
        for _name_j, document_vector_j in document_vectors.items():
            value_i_j = cosine_similarity(document_vector_i, document_vector_j)
            matrix_row_i.append(value_i_j)
        matrix.append(matrix_row_i)
    return [matrix, file_names]

# cos(theta) = d_1 dot d_2 / vect_mag(d_1) * vect_mag(d_2)
# input: document vector (list) x 2
# output: cosine similarity of vecotrs (num)
def cosine_similarity(doc_vec_1, doc_vec_2):
    dot_prod = dot_product(doc_vec_1, doc_vec_2)
    if not dot_prod:
        print("Document Vecotors are not the same length")
        return False
    vec_1_mag = vector_magnitude(doc_vec_1)
    vec_2_mag = vector_magnitude(doc_vec_2)
    vec_mag_prod = vec_1_mag * vec_2_mag
    if vec_mag_prod == 0:
        return 0
    cosine = dot_prod / vec_mag_prod
    return cosine

def vector_magnitude(vector):
    vec_mag_sqared = 0
    for value in vector:
        vec_mag_sqared += value**2
    vec_mag = math.sqrt(vec_mag_sqared)
    return vec_mag

# input: two vecotrs of the same length
# output: dot product of vectors (num)
def dot_product(vec_1, vec_2):
    #sum of di1*di2
    dot_prod = 0
    length_1 = len(vec_1)
    length_2 = len(vec_2)
    if length_1 != length_2:
        return False
    for i in range(length_1):
        di1 = vec_1[i]
        di2 = vec_2[i]
        dot_prod += di1 * di2
    return dot_prod
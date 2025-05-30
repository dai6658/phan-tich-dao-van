
from underthesea import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from model_utils import preprocess_sentence, remove_numbered_prefix

def compare_sentences(sentences_a, sentences_b, vec_a, vec_b, source_file, threshold):
    matches = []
    for i, vec1 in enumerate(vec_a):
        for j, vec2 in enumerate(vec_b):
            score = cosine_similarity([vec1], [vec2])[0][0]
            if score >= threshold:
                matches.append({
                    "cau_nghi": sentences_a[i],
                    "cau_nguon": sentences_b[j],
                    "nguon": source_file,
                    "diem": round(score, 4)
                })
    return matches

def analyze_plagiarism(file_suspect, source_files, model, read_file_fn, threshold=0.8):
    content_suspect = remove_numbered_prefix(read_file_fn(file_suspect))
    sentences_suspect = sent_tokenize(content_suspect)
    vec_suspect = model.encode([preprocess_sentence(s) for s in sentences_suspect])

    result = []
    for file_src in source_files:
        if file_src == file_suspect:
            continue
        content_src = remove_numbered_prefix(read_file_fn(file_src))
        sentences_src = sent_tokenize(content_src)
        vec_src = model.encode([preprocess_sentence(s) for s in sentences_src])
        result.extend(compare_sentences(sentences_suspect, sentences_src, vec_suspect, vec_src, file_src, threshold))
    return result

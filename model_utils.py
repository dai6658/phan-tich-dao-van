
import re
import string
from underthesea import word_tokenize
from underthesea import text_normalize
from sentence_transformers import SentenceTransformer

def load_stopwords(file_path="vietnamese-stopwords.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip() and " " not in line.strip())

stopwords_vn = load_stopwords()

def load_model():
    return SentenceTransformer("keepitreal/vietnamese-sbert")

def remove_numbered_prefix(text):
    return re.sub(r"(?m)^\s*\d+\.\s*", "", text)

def preprocess_sentence(sentence):
    sentence = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    sentence = text_normalize(sentence)
    words = word_tokenize(sentence)
    return " ".join([w for w in words if w not in stopwords_vn])



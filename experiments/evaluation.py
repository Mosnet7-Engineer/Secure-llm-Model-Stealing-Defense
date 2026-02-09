from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_similarity(orig, stolen):
    emb1 = model.encode(orig, convert_to_tensor=True)
    emb2 = model.encode(stolen, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).mean().item()

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_file(path):
    with open(path, "r") as f:
        return f.readlines()

def evaluate_similarity(file1, file2):
    data1 = load_file(file1)
    data2 = load_file(file2)

    scores = []
    for a, b in zip(data1, data2):
        emb1 = model.encode(a, convert_to_tensor=True)
        emb2 = model.encode(b, convert_to_tensor=True)
        score = util.cos_sim(emb1, emb2).item()
        scores.append(score)

    return sum(scores) / len(scores)


if __name__ == "__main__":
    score = evaluate_similarity(
        "results/baseline_outputs.txt",
        "results/defended_outputs.txt"
    )
    print(f"Similarity Score: {score}")

from sentence_transformers import SentenceTransformer, util
import os

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
    # 🔹 Hardcoded input files
    baseline_file = "results/baseline_outputs_200.txt" #Change the filename as well with the number
    defended_file = "results/defended_outputs_200.txt" #Change the number as well with the number

    # 🔹 Compute similarity
    score = evaluate_similarity(baseline_file, defended_file)

    # 🔹 Ensure results folder exists
    os.makedirs("results", exist_ok=True)

    # 🔹 Hardcoded output file
    output_file = "results/evaluation_200.txt"

    with open(output_file, "w") as f:
        f.write("Experiment: 200 queries\n") #Change the number query
        f.write(f"Baseline file: {baseline_file}\n")
        f.write(f"Defended file: {defended_file}\n")
        f.write(f"Similarity Score: {score}\n")

    # 🔹 Print to terminal
    print(f"Similarity Score: {score}")
    print(f"Saved to: {output_file}")

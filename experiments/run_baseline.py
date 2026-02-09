from attacks.query_generator import generate_queries
from attacks.extraction_pipeline import ModelExtractor

queries = generate_queries(50)
extractor = ModelExtractor()

outputs = []
for q in queries:
    out = extractor.query(q)
    outputs.append(out)

with open("results/baseline_outputs.txt", "w") as f:
    for o in outputs:
        f.write(o + "\n\n")

print("Baseline extraction complete.")

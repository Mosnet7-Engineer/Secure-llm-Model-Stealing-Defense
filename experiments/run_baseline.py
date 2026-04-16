from attacks.query_generator import generate_queries
from attacks.extraction_pipeline import ModelExtractor

queries = generate_queries(200) # Replace any numbers with ()
extractor = ModelExtractor()

outputs = []
for q in queries:
    out = extractor.query(q)
    outputs.append(out)

with open("results/baseline_outputs_200.txt", "w") as f: #Change the filename _100 or _50
    for o in outputs:
        f.write(o + "\n\n")

print("Baseline extraction complete.")

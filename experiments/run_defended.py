from attacks.query_generator import generate_queries
from attacks.extraction_pipeline import ModelExtractor
from defense.watermarking import apply_watermark

queries = generate_queries(50)
extractor = ModelExtractor()

outputs = []
for q in queries:
    out = extractor.query(q)
    out = apply_watermark(out)
    outputs.append(out)

with open("results/defended_outputs.txt", "w") as f:
    for o in outputs:
        f.write(o + "\n\n")

print("Defended extraction complete.")

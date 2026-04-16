import random

def generate_queries(n=1000):
    base_prompts = [
        "Explain cybersecurity to a beginner.",
        "What is a firewall?",
        "How does encryption work?",
        "Explain machine learning in simple terms.",
        "What is penetration testing?",
        "How do LLMs work?",
        "Explain zero trust security."
    ]

    queries = []
    for _ in range(n):
        q = random.choice(base_prompts)
        q += " Give a detailed explanation."
        queries.append(q)

    return queries

if __name__ == "__main__":
    qs = generate_queries(100)
    print(qs[:5])


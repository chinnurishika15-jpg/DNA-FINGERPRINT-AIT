# DNA Fingerprinting AI Analysis
# This is a simple demonstration of how AI can help analyze DNA sequences

# Sample DNA sequences
sample_dna = {
    "Person_A": "ATCGTACGATCG",
    "Person_B": "ATCGTTCGATGG",
    "Person_C": "ATCGTACGATGG"
}

# Function to compare two DNA sequences
def compare_dna(seq1, seq2):
    matches = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            matches += 1
    similarity = matches / len(seq1) * 100
    return similarity

# Analyze all pairs
persons = list(sample_dna.keys())
for i in range(len(persons)):
    for j in range(i+1, len(persons)):
        p1 = persons[i]
        p2 = persons[j]
        similarity = compare_dna(sample_dna[p1], sample_dna[p2])
        print(f"Similarity between {p1} and {p2}: {similarity:.2f}%")

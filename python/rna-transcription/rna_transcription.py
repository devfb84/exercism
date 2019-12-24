dna_to_rna = {"G": "C",
              "C": "G",
              "T": "A",
              "A": "U"}


def to_rna(dna_strand):
    rna = []

    for char in dna_strand:
        rna.append(dna_to_rna[char])

    return "".join(rna)

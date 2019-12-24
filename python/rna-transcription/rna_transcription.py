dna_to_rna = {"G": "C",
              "C": "G",
              "T": "A",
              "A": "U"}


def to_rna(dna_strand):
    return dna_strand.translate(str.maketrans(dna_to_rna))

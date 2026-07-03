# Amino acid weights (simplified)
aa_weights = {
    'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1,
    'C': 121.2, 'Q': 146.2, 'E': 147.1, 'G': 75.1,
    'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
    'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1,
    'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
}

hydrophobic = set("AILMFWV")
charged = set("DEKR")


def amino_acid_composition(seq):
    comp = {}
    for aa in seq:
        comp[aa] = comp.get(aa, 0) + 1
    return comp


def molecular_weight(seq):
    return sum(aa_weights.get(aa, 0) for aa in seq)


def hydrophobicity_score(seq):
    if len(seq) == 0:
        return 0
    return sum(1 for aa in seq if aa in hydrophobic) / len(seq)


def charged_ratio(seq):
    if len(seq) == 0:
        return 0
    return sum(1 for aa in seq if aa in charged) / len(seq)


def find_motifs(seq):
    motifs = []

    for i in range(len(seq) - 2):
        if seq[i] == "N" and seq[i+1] != "P" and seq[i+2] in ["S", "T"]:
            motifs.append(f"N-glyco site at position {i+1}")

    return motifs

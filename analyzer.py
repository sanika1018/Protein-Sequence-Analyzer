import sys
from utils.stats import *


def read_fasta(file_path):
    sequences = {}
    header = None
    seq = ""

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if header:
                    sequences[header] = seq
                header = line[1:]
                seq = ""
            else:
                seq += line

        if header:
            sequences[header] = seq

    return sequences


def analyze(name, seq):
    print("\n==============================")
    print("🧬 Protein:", name)
    print("==============================")

    comp = amino_acid_composition(seq)
    mw = molecular_weight(seq)
    hydro = hydrophobicity_score(seq)
    charge = charged_ratio(seq)
    motifs = find_motifs(seq)

    result = f"""
Protein Name: {name}
Length: {len(seq)}

Amino Acid Composition: {comp}
Molecular Weight: {mw:.2f} Da
Hydrophobicity Score: {hydro:.3f}
Charged Residue Ratio: {charge:.3f}

Motifs Found:
{motifs if motifs else 'None'}
"""

    print(result)
    return result


def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python3 analyzer.py <fasta_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    sequences = read_fasta(file_path)

    if not sequences:
        print("❌ No valid sequences found")
        sys.exit(1)

    full_report = ""

    for name, seq in sequences.items():
        full_report += analyze(name, seq)

    with open("output/report.txt", "w") as f:
        f.write(full_report)

    print("\n📄 Report saved in output/report.txt")


if __name__ == "__main__":
    main()

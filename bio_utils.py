# Standard Translation Table: RNA Codons to Amino Acid Conversion

CODON_TABLE= {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU':
        'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# Monoisotopic mass values (in Daltons) for each amino acid minus a water molecule
AMINO_ACID_WEIGHTS = {
    'A': 71.04, 'R': 156.10, 'N': 114.04, 'D': 115.03, 'C': 103.01,
    'E': 129.04, 'Q': 128.06, 'G': 57.02, 'H': 137.06, 'I': 113.08,
    'L': 113.08, 'K': 128.09, 'M': 131.04, 'F': 147.07, 'P': 97.05,
    'S': 87.03, 'T': 101.05, 'W': 186.08, 'Y': 163.06, 'V': 99.07,
    '*': 0.00  # The stop character adds no weight
}

from bio_utils import CODON_TABLE
from bio_utils import AMINO_ACID_WEIGHTS


seq= 'GTCATGTTCGCCTGCCCTAGATAACTGGCTTCCTAGGTACGCT'

#Print number of nucleotides
print(f"Sequence Length:{str(len(seq))}\n")

#Count bases per nucleotide
def count_all_bases(seq):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    # Loop through the string (converted to uppercase to avoid case errors)
    for base in seq.upper():
        if base in counts:
            counts[base] += 1
    return counts

base_count = '\n'.join(f"{letter}: {count}" for letter, count in count_all_bases(seq).items())
print(f"{base_count}\n")

#find the complement of DNA sequence
comp= seq.upper().translate(str.maketrans("ATCG", "TAGC"))[:]
print(f"Complementary Strand:\n{comp}\n")

#find the reverse complement of DNA sequence
reverse_comp= comp[::-1]
print(f"Reverse Complementary Strand:\n{reverse_comp}\n")

#find the RNA sequence
def dna_to_rna(seq):
    return seq.upper().replace("T", "U")
rna_seq= dna_to_rna(seq)
print(f"RNA Sequence:\n{rna_seq}\n")


#find GC content
def get_gc_content(seq):
    gc_count= seq.upper().count("G") + seq.upper().count("C")
    return (gc_count / len(seq)) * 100

print(f"GC content:\n{get_gc_content(seq):.2f}%""\n")

#find AT content
def get_at_content(seq):
    at_count = seq.upper().count("A") + seq.upper().count("T")
    return (at_count / len(seq)) * 100

print(f"AT content:\n{get_at_content(seq):.2f}%""\n")

#translate RNA into Protein
def rna_to_protein(rna_seq):
    protein= []

    #try to find the start codon
    start_index= rna_seq.find("AUG")

    if start_index == -1:
        print("No start codon found. Translating from the beginning of the sequence.")
        start_index = 0
    else:
        print(f"Start codon found at position {start_index}")

    #run the translation loop
    for i in range(start_index, len(rna_seq), 3):
        codon= rna_seq[i:i + 3]
        if len(codon) < 3:
            break

        amino_acid= CODON_TABLE.get(codon)

        if amino_acid == 'Stop':
            print(f"Stop codons found: '{codon}'\n")
            break

        else:
            protein.append(amino_acid)

    return "".join(protein)

amino_acid_chain= rna_to_protein(rna_seq)
print(f"Protein Sequence:\n{amino_acid_chain}\n")

#get the molecular weight of the protein sequence
def mol_weight(amino_acid_chain):

    if not amino_acid_chain:
        return 0.0

    total_weight= 0.0
    unknown_count= 0

    for aa in amino_acid_chain:
        weight= AMINO_ACID_WEIGHTS.get(aa)

        if weight:
            total_weight += weight
        else:
            #if protein contains an error character like "X"
            print(f"⚠️ Warning: Unknown amino acid character '{aa}' ignored in weight calculation.")
            unknown_count += 1

    #subtract water lost during peptide bond formation
    num_amino_acids= len(amino_acid_chain) - unknown_count
    if num_amino_acids > 1:
        water_loss= (num_amino_acids - 1) * 18.015
        total_weight -= water_loss

    return total_weight
protein_weight= mol_weight(amino_acid_chain)
print(f"Protein Molecular Weight: {protein_weight:.2f} Da")


#TODO add mol weight calculator,ORF finder, melting temp and hydrophobicity index
#TODO update readme pep88, dna seq/ project overview to reflect changes,
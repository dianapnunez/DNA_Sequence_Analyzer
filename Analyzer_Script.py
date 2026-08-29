from Genetic_Code import Codon_Table

seq= 'GTCTTCGCCTGCCCTAGATAAATGCTGGCTTCCTAGGTACGCT'

#Print number of nucleotides
print("Length:" + str(len(seq)), "\n")

#Count bases per nucleotide
def count_all_bases(seq):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    # Loop through the string (converted to uppercase to avoid case errors)
    for base in seq.upper():
        if base in counts:
            counts[base] += 1
    return counts

base_count = '\n'.join(f"{letter}: {count}" for letter, count in count_all_bases(seq).items())
print(base_count + "\n")

#find the RNA sequence
def DNA_to_RNA(seq):
    return seq.upper().replace("T", "U")
RNA_seq= DNA_to_RNA(seq)
print("RNA sequence: " + "\n" + RNA_seq + "\n")

#find the reverse complement of DNA sequence
reverse_comp= seq.upper().translate(str.maketrans("ATCG", "TAGC"))[::-1]
print("Reverse Complement: " + "\n" + reverse_comp + "\n")


#find GC content
def get_GC_content(seq):
    GC_count= seq.upper().count("G") + seq.upper().count("C")
    return (GC_count / len(seq)) * 100

print(f"GC content:\n{get_GC_content(seq):.2f}%""\n")

#find AT content (I could have used 100-GC_count)
def get_AT_content(seq):
    AT_count = seq.upper().count("A") + seq.upper().count("T")
    return (AT_count / len(seq)) * 100

print(f"AT content:\n{get_AT_content(seq):.2f}%""\n")

#translate RNA into Protein
def RNA_to_protein(RNA_seq):
    protein= []
    for i in range(0, len(RNA_seq), 3):
        codon= RNA_seq[i:i+3]
        amino_acid= Codon_Table.get(codon)
        if amino_acid == 'Stop':
            protein.append('*')
            print(f"Stop codons found: '{codon}'\n")
            break
        if amino_acid:
            protein.append(amino_acid)
    return "".join(protein)

amino_acid_chain= RNA_to_protein(RNA_seq)
print("Protein Sequence: " + "\n" + amino_acid_chain)


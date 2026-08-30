# 🧬 DNA Sequence Analyzer

A Python-based bioinformatics project that performs fundamental DNA sequence analysis. The application calculates nucleotide composition, computes GC and AT content, generates a complement and reverse-complement strand, transcribes DNA into RNA, translates RNA into protein, calculates protein molecular weight, and provides a hydrophobicity index score. 

This project combined multiple Rosalind bioinformatics problems into a single, cohesive application. This project was a learning exercise in Python programming and Bioinformatics, demonstrating how computational methods can be applied to molecular biology.

---

# 📖 Project Overview

---

DNA sequence analysis is one of the core tasks in bioinformatics. This project accepts a DNA sequence and performs multiple analyses commonly used in genetics and molecular biology.

The program currently includes:
* Nucleotide counts (A, T, G, C)
* Sequence length calculation
* GC content calculation
* AT content calculation
* Complement DNA strand generation 
* Reverse Complement strand generation
* DNA to RNA transcription
* RNA to protein translation
* `Start` and `Stop` codon detection
* Molecular weight calculation
* Hydrophobicity Index Score

---

# 📂 Project Structure

---

```text
DNA_Sequence_Analyzer/
├── analyzer_script.py
├── bio_utils.py
├── LICENSE
├── README.md
└── .gitignore
```

### File Description

| File                 | Purpose                                                                                                                            |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| `analyzer_script.py` | Controls the program execution and contains all DNA analysis functions                                                             |
| `bio_utils.py`       | Serves as a reference module providing lookup data for RNA translation, amino acid molecular weights, and hydrophobicity profiling |
| `README.md`          | Project documentation                                                                                                              |

---

# ⚙️ Technologies Used

---

* Python 3
* Git
* GitHub

---

# 🚀 Installation & Execution

---

1. Clone the repository:
```bash
git clone https://github.com
```
2. Move into the project directory:
```bash
cd DNA_Sequence_Analyzer
```
3. Run the program:
```bash
python DNA_Sequence_Analyzer.py
```

---

# 🧬 Example DNA Sequence

---

```text
GTCTTCGCCTGCCCTAGAAATGCTGGCTTCCTAGGTACGCT
```

---

# 📊 Example Output

---

```text
Sequence Length:43

A: 7
T: 13
C: 13
G: 10

Complementary Strand:
CAGTACAAGCGGACGGGATCTATTGACCGAAGGATCCATGCGA

Reverse Complementary Strand:
AGCGTACCTAGGAAGCCAGTTATCTAGGGCAGGCGAACATGAC

RNA Sequence:
GUCAUGUUCGCCUGCCCUAGAUAACUGGCUUCCUAGGUACGCU

GC content:
53.49%

AT content:
46.51%

Start codon found at position 3
Stop codons found: 'UAA'

Protein Sequence:
MFACPR

Protein Molecular Weight: 615.24 Da

Hydrophobicity Index (GRAVY): 0.48


```

---

# 🧠 Biological Concepts Used

---

This project applies several important concepts from molecular biology, including:
* **DNA Structure & Composition:** Counting bases and measuring sequence length
* **Complementary Base Pairing:** Generating the complement strand relies on the specific hydrogen bonding rules where A pairs with T and C pairs with G.
* **Transcription:** Converting DNA to RNA   
* **Translation:** Converting RNA to protein. Finding AUG simulates scanning for the start codon (Methionine), while terminating at specific triplets simulates stop codons releasing the peptide chain.
* **Dehydration Synthesis:** Subtracting water weight (18.015 Da) for each peptide bond accounts for the condensation reaction that links amino acids together.
* **Protein Hydrophobicity:** Reveals whether the protein prefers aqueous environments or lipid membranes (transmembrane regions).
---

# 🎯 Learning Outcomes

---

This project helped me practice:
* Python programming
* Functions and modular programming
* String manipulation, translation mappings (`str.maketrans`), and inversion slicing (`[::-1]`)
* Dictionaries, functions and loops (`.get()`)
* Git version control and repository hosting profiles

---

# 🔮 Future Improvements

---

Planned enhancements include:
* Melting temperature calculator
* FASTA file parsing and ingestion pipelines
* Error validation traps to flags non-canonical code bugs (such as numbers or unknown characters)
* Generating data visualization charts of nucleotide distributions using Matplotlib
* Output options to save analysis summaries into structured CSV files

---

# 🤝 Contributing

---

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, create a new branch, and submit a pull request.

---

# 📜 License

---

This project is licensed under the MIT License.

---

# ⭐ Support

---

If you found this project useful or interesting, consider giving it a ⭐ Star on GitHub.

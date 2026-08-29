# 🧬 DNA Sequence Analyzer

A Python-based bioinformatics project that performs fundamental DNA sequence analysis. The application calculates nucleotide composition, computes GC content, generates a reverse-complement strand, transcribes DNA into RNA, and translates RNA into protein. 

This project combined multiple Rosalind bioinformatics problems into a single, cohesive application. This project was a learning exercise in Python programming and Bioinformatics, demonstrating how computational methods can be applied to molecular biology.

---

# 📖 Project Overview

---

DNA sequence analysis is one of the core tasks in bioinformatics. This project accepts a DNA sequence and performs multiple analyses commonly used in genetics and molecular biology.

The program currently includes:
* Nucleotide counting (A, T, G, C)
* Sequence length calculation
* GC Content percentage calculation
* Reverse Complement antisense generation
* DNA to RNA transcription
* RNA to protein translation with `Stop` codon detection

---

# 📂 Project Structure

---

```text
DNA_Sequence_Analyzer/
├── DNA_Sequence_Analyzer.py
├── Genetic_Code.py
├── LICENSE
├── README.md
└── .gitignore
```

### File Description

| File | Purpose |
| :--- | :--- |
| `DNA_Sequence_Analyzer.py` | Controls the program execution and contains all DNA analysis functions |
| `Genetic_Code.py` | Stores the genetic code dictionary used for protein translation |
| `README.md` | Project documentation |

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
Length: 41 

A: 9
T: 10
C: 13
G: 9

RNA sequence: 
GUCUUCGCCUGCCCUAGAAAUGCUGGCUUCCUAGGUACGCU

Reverse Complement: 
AGCGTACCTAGGAAGCCAGCATTTCTAGGGCAGGCGAAGAC

GC content:
53.66%

Protein Sequence: 
VFACPRNAGFLGTL
```

---

# 🧠 Biological Concepts Used

---

This project applies several important concepts from molecular biology, including:
* **DNA Primary Structure:** Sequence metrics and length checking.
* **Complementary Base Pairing:** Antisense strand creation via string dictionary translations.
* **Central Dogma of Molecular Biology:** Simulating transcription loops (DNA ➔ RNA) and translational step-frames.
* **Codon Logic:** Iterating sequences in steps of 3 to fetch matching amino acid residues.
* **Translational Termination:** Breaking string assembly structures dynamically when matching a biological `Stop` codon value.

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
* Complete 64-codon handling checks
* Multi-line FASTA file parsing and ingestion pipelines
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

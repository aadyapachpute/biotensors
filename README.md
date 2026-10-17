# BIOTENSORS

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Bioinformatics](https://img.shields.io/badge/Field-Bioinformatics-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


An open-source computational biology pipeline bridging biological sequence analysis with numerical linear algebra, structural data parsing, and modular Python engineering.

## Overview

`biotensors` is a first-principles computational biology pipeline built to process, analyze, and map biological sequence and structural data without relying on heavy black-box abstractions. 

Starting from NCBI RefSeq accession queries, the pipeline executes manual sequence parsing, GC content distribution metrics, GenBank CDS extraction, and 3D structural distance matrix calculations.

*Note: This project is built for educational, research, and portfolio development purposes.*

## Features

* Programmatic gene and mRNA sequence retrieval via NCBI Entrez APIs (`requests`)
* Manual FASTA file parsing and nucleotide composition analysis
* GC content calculation and comparative Matplotlib visualizations
* GenBank record ingestion and annotated CDS extraction
* Structural bioinformatics: PDB file coordinate parsing ($x, y, z$)
* Pairwise Euclidean distance matrix generation for residue-to-residue spatial analysis
* Structured CLI entry points via `argparse`
* Automated testing architecture via `pytest`


## Project structure

```text
biotensors/
├── data/
│   ├── BRCA1.fasta
│   ├── KRAS.fasta
│   ├── TP53.fasta
│   └── gc_content_comparison.png
│
├── reports/
│   ├── TP53_mutation_report.txt
│   ├── KRAS_mutation_report.txt
│   ├── BRCA1_mutation_report.txt
│   └── mutation_summary.csv
│
├── scripts/
│   ├── cli.py
│   ├── analyze.py
│   ├── fetch_gene.py
│   ├── test_cds.py
│   ├── visualize.py
│   ├── p53_analyzer.py
│   └── kras_analyzer.py
│
├── src/
│   ├── ncbi/
│   │   ├── fetch.py
│   │   ├── search.py
│   │   └── cds.py
│   │
│   └── mutations/
│       └── known_mutations.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

Additional concept notes are available in [`docs/concepts.md`](docs/concepts.md).

## Installation

Clone the repository:

```bash
git clone [https://github.com/aadyapachpute/biotensors.git](https://github.com/aadyapachpute/biotensors.git)
cd biotensors
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
pandas
requests
matplotlib
pytest
```

## Usage

### Analyze a single gene

```bash
python -m scripts.cli --gene TP53
```

### Analyze multiple genes

```bash
python -m scripts.cli --genes TP53 KRAS BRCA1
```

The pipeline will:

1. Search for the gene in NCBI
2. Fetch a RefSeq mRNA FASTA record
3. Save the sequence to the `data/` directory
4. Perform nucleotide and GC content analysis
5. Retrieve the GenBank record
6. Extract annotated CDS protein information
7. Run known mutation site checks
8. Generate text reports
9. Generate a CSV summary file

## Example terminal output

```text
Searching for TP53...
Selected RefSeq: NM_001407264.1

Length: 2522 bp
GC Content: 52.78%

Using annotated CDS protein for mutation analysis.
Protein source: Annotated CDS protein
Protein length: 393 aa

--- Known Mutation Check ---
R175H: Normal (R at position 175)
R248Q: Normal (R at position 248)

Mutation report saved to reports/TP53_mutation_report.txt
CSV summary saved to reports/mutation_summary.csv
```

## Example CSV output

```csv
gene,sequence_length,protein_length,protein_source,gc_content,known_sites_checked,mutations_detected,different_variants
TP53,2522,393,Annotated CDS protein,52.78,2,0,0
```

## Mutation reports

For supported genes, the pipeline creates a text report in the `reports/` directory.

Example:

```text
=== Mutation Analysis Report ===

Gene: TP53
Protein length: 393 aa
Known mutation sites checked: 2

R175H:
  Position: 175
  Expected: R
  Observed: R
  Known mutation: H
  Status: Normal
  Type: Missense
  Info: Common tumor suppressor mutation

Summary:
  Known mutations detected: 0
  Different variants found: 0
```

## Visualization

![GC content comparison across cancer-associated genes](./data/gc_content_comparison.png)

The project includes a visualization script for comparing GC content across selected cancer-associated genes.


Run:

```bash
python -m scripts.visualize
```

Output:

```text
data/gc_content_comparison.png
```


## Author

Aadya Pachpute




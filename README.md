# Flip2Mol

Flip2Mol is a machine learning project developed for the course **DIT892 Project Course** in collaboration with AstraZeneca. The system aims to convert molecular fingerprints back into SMILES (Simplified Molecular Input Line Entry System) representations, enabling reconstruction of molecular structures from fingerprint data. This project explores the challenging inverse problem of molecular fingerprint decoding using modern machine learning approaches. For this project we analyzed the affect of ECFP4 fingerprint bit flipping on COX2 and Janus kinase inhibitors.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Technologies Used](#technologies-used)
4. [Deliverables](#deliverables)

---

## Getting Started

These instructions will help you set up Flip2Mol for development and testing purposes.

### Prerequisites

- Python
- Git
- Conda

---

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/NilsDunlop/Flip2Mol.git
cd Flip2Mol
```

2. **Create and Activate Conda Environment**
```bash
bash
conda env create -f environment.yml
conda activate fingerprint2smiles
```

3. **Run Jupyter Notebooks**
After setting up the environment, you can run the Jupyter notebooks located in the `src` directory:

---

## Technologies Used

- **[Python](https://www.python.org/)**
- **[RDKit](https://www.rdkit.org/)**
- **[Pandas](https://pandas.pydata.org/)**
- **[NumPy](https://numpy.org/)**
- **[Conda](https://docs.conda.io/)**
- **[MolForge](https://github.com/MolForge)**
- **[Jupyter Notebooks](https://jupyter.org/)**

---

## Deliverables

- [Project Report](./deliverables/Project_Report.pdf)
- [Presentation](./deliverables/Presentation.pdf)

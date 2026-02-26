# 🚀 TP02 -- Efficient Processing of Large CSV Files (5GB+) in Python

## 📌 Project Overview

Handling large-scale datasets is a fundamental challenge in Big Data
engineering. This project demonstrates how to efficiently process CSV
files larger than 5GB in Python without causing:

-   Memory overflow (Out-of-Memory errors)
-   System crashes
-   Performance degradation

Instead of loading the entire dataset into memory, optimized techniques
are applied to ensure stability, scalability, and performance.

------------------------------------------------------------------------

## 🎯 Objectives

-   Process a CSV dataset larger than 5GB.
-   Implement three optimized data-handling techniques.
-   Evaluate and compare:
    -   Execution time
    -   Storage size
    -   Memory efficiency
-   Demonstrate practical Big Data processing strategies.

------------------------------------------------------------------------

## 📂 Project Structure

    BigData_TP02/
    │
    ├── data/
    │   └── big_5gb_dataset.csv
    │
    ├── src/
    │   ├── chunk_reader.py
    │   ├── dask_reader.py
    │   ├── compression_test.py
    │   └── utils.py
    │
    ├── results/
    │   └── comparison.txt
    │
    ├── requirements.txt
    └── README.md


------------------------------------------------------------------------

## 🛠 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/BigData_TP02.git cd
BigData_TP02

### 2️⃣ Create a Virtual Environment

python -m venv venv

### 3️⃣ Activate Environment

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

### 4️⃣ Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 📊 Implemented Methods

### 1️⃣ Pandas with Chunking

Processes the dataset in small chunks instead of loading it entirely
into memory.

Example:

import pandas as pd

for chunk in pd.read_csv("big_5gb_dataset.csv", chunksize=100000):
process(chunk)

Advantages: - Prevents memory overflow - Stable and reliable - Easy
implementation

------------------------------------------------------------------------

### 2️⃣ Dask DataFrame

Uses parallel computing to handle large datasets efficiently.

Example:

import dask.dataframe as dd

df = dd.read_csv("big_5gb_dataset.csv") result = df.describe().compute()

Advantages: - Multi-core processing - Faster execution - Designed for
Big Data workloads

------------------------------------------------------------------------

### 3️⃣ File Compression (Gzip)

Reduces storage size by compressing the dataset.

Example:

import gzip import shutil

with open("big_5gb_dataset.csv", 'rb') as f_in: with
gzip.open("big_5gb_dataset.csv.gz", 'wb') as f_out:
shutil.copyfileobj(f_in, f_out)

Advantages: - Reduces disk usage - Facilitates data transfer - Maintains
data integrity

------------------------------------------------------------------------

## 📈 Performance Comparison

The evaluation criteria include:

-   Execution Time (seconds)
-   File Size (GB)
-   Memory Usage

All experimental results are stored in:

results/comparison.txt

------------------------------------------------------------------------

## 🧠 Conclusion

This project demonstrates that:

-   Chunk-based processing effectively prevents memory overflow.
-   Dask significantly improves performance through parallel execution.
-   Compression reduces storage requirements without data loss.
-   Efficient Big Data handling is essential for Machine Learning and AI
    pipelines.

------------------------------------------------------------------------

## 🧪 Technologies Used

-   Python 3.x
-   Pandas
-   Dask
-   Gzip
-   Virtual Environment (venv)

------------------------------------------------------------------------

## 👨‍💻 Author

Abdelhakim Berrim Master's Degree -- Cybersecurity Course: Big Data /
Data Processing

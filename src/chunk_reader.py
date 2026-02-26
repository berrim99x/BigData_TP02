import pandas as pd
import time
import psutil
import os

file_path = "../data/big_5gb_dataset.csv"
output_file = "../results/comparison.txt"

process = psutil.Process(os.getpid())

start = time.time()

chunk_size = 100000
total_rows = 0

max_memory = 0

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_rows += len(chunk)
    current_memory = process.memory_info().rss / (1024 ** 2)
    max_memory = max(max_memory, current_memory)

end = time.time()
execution_time = end - start

with open(output_file, "w") as f:
    f.write("===== CHUNK METHOD =====\n")
    f.write(f"Total Rows: {total_rows}\n")
    f.write(f"Execution Time: {execution_time:.2f} seconds\n")
    f.write(f"Max RAM Usage: {max_memory:.2f} MB\n\n")

print("Chunk results saved.")
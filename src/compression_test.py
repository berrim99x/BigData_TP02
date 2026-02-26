import pandas as pd
import time
import os
import psutil

file_path = "../data/big_5gb_dataset.csv"
compressed_path = "../data/big_5gb_dataset.csv.gz"
output_file = "../results/comparison.txt"

process = psutil.Process(os.getpid())

start = time.time()

df = pd.read_csv(file_path)
df.to_csv(compressed_path, index=False, compression="gzip")

current_memory = process.memory_info().rss / (1024 ** 2)

end = time.time()
execution_time = end - start

original_size = os.path.getsize(file_path) / (1024**3)
compressed_size = os.path.getsize(compressed_path) / (1024**3)

with open(output_file, "a") as f:
    f.write("===== COMPRESSION METHOD =====\n")
    f.write(f"Compression Time: {execution_time:.2f} seconds\n")
    f.write(f"Original Size: {original_size:.2f} GB\n")
    f.write(f"Compressed Size: {compressed_size:.2f} GB\n")
    f.write(f"RAM Usage: {current_memory:.2f} MB\n\n")

print("Compression results saved.")
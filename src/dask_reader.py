import dask.dataframe as dd
import time
import psutil
import os

file_path = "../data/big_5gb_dataset.csv"
output_file = "../results/comparison.txt"

process = psutil.Process(os.getpid())

start = time.time()

df = dd.read_csv(file_path)
total_rows = df.shape[0].compute()

current_memory = process.memory_info().rss / (1024 ** 2)

end = time.time()
execution_time = end - start

with open(output_file, "a") as f:
    f.write("===== DASK METHOD =====\n")
    f.write(f"Total Rows: {total_rows}\n")
    f.write(f"Execution Time: {execution_time:.2f} seconds\n")
    f.write(f"RAM Usage: {current_memory:.2f} MB\n\n")

print("Dask results saved.")
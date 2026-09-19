import os
from datasets import load_dataset
import pandas as pd

def fetch_and_save_data(output_dir="data/raw"):
    os.makedirs(output_dir, exist_ok=True)
    print("Descargando dataset desde Hugging Face...")
    
    dataset = load_dataset("mrcksggcfc/store-sales-time-series-forecasting")
    
    for split_name in dataset.keys():
        df = dataset[split_name].to_pandas()
        file_path = os.path.join(output_dir, f"{split_name}.parquet")
        df.to_parquet(file_path, index=False)
        print(f"Guardado: {file_path} ({len(df):,} filas)")

if __name__ == "__main__":
    fetch_and_save_data()

import os
import yaml
import pandas as pd
import argparse
from load_data import read_params, load_and_save
from get_data import read_params

def clean(config_path):
    config = read_params(config_path)

    raw_data_path = config["load_data"]["raw_dataset_csv"]
    clean_data_path = config["clean_data"]["clean_dataset_csv"]

    df = pd.read_csv(raw_data_path, sep=",")
    clean = df. dropna() 
    clean.to_csv(clean_data_path, sep=",", index=False, encoding="utf-8")
    


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    clean(config_path=parsed_args.config)    
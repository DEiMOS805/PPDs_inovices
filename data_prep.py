import re
import sys
import numpy as np
import pandas as pd


def get_file_name(path):
    match = re.search(r"([\w\-\.]+)$", path)
    if match:
        return match.group(1)
    else:
        return None


def new_output_path(output_path, file_name):
    return (
        f"{output_path}/{file_name}"
        if "/" in output_path
        else f"{output_path}{file_name}"
    )


def clean(df):
    # file.loc[1, "Empresa"] = re.sub(r"\*", "", file.loc[1, "Empresa"])
    for header in df.columns:
        # print(header)
        for i in range(len(df[header])):
            if not isinstance(file.loc[i, header], str):
                continue
            elif file.loc[i, header] == " ":
                file.loc[i, header] = re.sub(r" ", "NA", file.loc[i, header])
            else:
                file.loc[i, header] = re.sub(r"\*", "", file.loc[i, header])
                file.loc[i, header] = re.sub(r" ", "", file.loc[i, header])
    return df


if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2]

    file = pd.read_csv(file_path, sep=",", encoding="utf-8")
    cleaned_df = clean(file)

    file_name = get_file_name(file_path)
    output_path = new_output_path(output_path, file_name)

    cleaned_df.to_csv(output_path, sep=",", encoding="utf-8", index=False)

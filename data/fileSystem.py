from pathlib import Path
import json
import shutil
import pandas as pd
import csv
from pandas import DataFrame


def create_dir_if_not_exists(paths: list):
    if type(paths) is not list:
        paths = [paths]
    for p in paths:
        if p.is_dir():
            print(f"dir {p} exists")
        else:
            p.mkdir()
            print(f"dir {p} created")


def copy_file(source: Path, destination: Path):
    shutil.copyfile(src=source, dst=destination)


def delete_file(file: Path):
    if file.is_file():
        file.unlink()
        print(f"deleted {file}")


def create_file(file: Path):
    with file.open("w"):
        print(f"created {file}")


def file_to_str(file: Path, encoding: str = "utf-8") -> str:
    with open(file, "r", encoding=encoding) as f:
        lines = f.readlines()
    return "".join(lines)


def str_to_file(file: Path, input: str, encoding: str = "utf-8"):
    with open(file, "w", encoding=encoding) as f:
        f.write(input)


def json_to_dict(file: Path) -> dict:
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data


def dict_to_json(data: dict, file: Path):
    with open(file, "w") as json_file:
        json.dump(data, json_file)


def csv_to_df(filePath: Path, delimiter: str = ";") -> DataFrame:
    df = pd.read_csv(filePath, delimiter=delimiter)
    df.fillna("", inplace=True)
    return df


def csv_to_list_of_dicts(filePath: Path, delimiter: str = ";") -> list[dict]:
    df = pd.read_csv(filePath, delimiter=delimiter)
    df.fillna("", inplace=True)
    dict = df.to_dict(orient="records")
    return dict


def csv_to_list_of_lists(
    filePath: Path, delimiter: str = ";", includeHeards: bool = True
) -> list[list]:
    rows = []
    with open(filePath, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=delimiter)
        header = [next(reader)]
        for row in reader:
            rows.append(row)
    if includeHeards:
        return header + rows
    else:
        return rows


def list_of_lists_to_csv(filePath: Path, data: list[list], delimiter: str = ","):
    with open(filePath, "w", encoding="utf-8-sig", newline="") as file:
        csvwriter = csv.writer(file, delimiter=delimiter)
        csvwriter.writerows(data)


def list_files(
    path: Path, datatype: str = None, keyword: str = None, nameOnly: bool = False
) -> list:
    output = list()
    for file in path.iterdir():
        ok = True
        if datatype is not None:
            if file.suffix != datatype:
                ok = False
        if keyword is not None:
            if keyword not in file.name:
                ok = False
        if ok:
            if nameOnly:
                output.append(file.name)
            else:
                output.append(file)

    return output


def df_to_file(df: DataFrame, filePath: Path, seperator=";"):
    fileType = filePath.suffix
    if fileType == ".csv":
        df.to_csv(filePath, index=False, sep=seperator, encoding="utf-8-sig")
    elif fileType == ".html":
        df.to_html(filePath)
    else:
        raise TypeError(f"no supported file type recognized for { filePath }")

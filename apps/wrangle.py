from re import search, findall
from os import listdir, path
import pandas as pd
from winreg import *


SCENARIOS = {
    "Easy": {
        "Pasu Voltaic Easy": ["Clicking", "Dynamic", 0], "B180 Voltaic Easy": ["Clicking", "Dynamic", 0],
        "Popcorn Voltaic Easy": ["Clicking", "Dynamic", 0], "ww3t Voltaic": ["Clicking", "Static", 0],
        "1w4ts Voltaic": ["Clicking", "Static", 0], "6 Sphere Hipfire Voltaic": ["Clicking", "Static", 0],
        "Smoothbot Voltaic Easy": ["Tracking", "Precise", 0], "Air Angelic 4 Voltaic Easy": ["Tracking", "Precise", 0],
        "PGTI Voltaic Easy": ["Tracking", "Precise", 0], "FuglaaXYZ Voltaic Easy": ["Tracking", "Reactive", 0],
        "Ground Plaza Voltaic Easy": ["Tracking", "Reactive", 0], "Air Voltaic Easy": ["Tracking", "Reactive", 0],
        "patTS Voltaic Easy": ["Switching", "Speed", 0], "psalmTS Voltaic Easy": ["Switching", "Speed", 0],
        "voxTS Voltaic Easy": ["Switching", "Speed", 0], "kinTS Voltaic Easy": ["Switching", "Evasive", 0],
        "B180T Voltaic Easy": ["Switching", "Evasive", 0], "Smoothbot TS Voltaic Easy": ["Switching", "Evasive", 0],
    },
    "Hard": {
        "Pasu Voltaic": ["Clicking", "Dynamic", 0], "B180 Voltaic": ["Clicking", "Dynamic", 0],
        "Popcorn Voltaic": ["Clicking", "Dynamic", 0], "ww3t Voltaic": ["Clicking", "Static", 0],
        "1w4ts Voltaic": ["Clicking", "Static", 0], "6 Sphere Hipfire Voltaic": ["Clicking", "Static", 0],
        "Smoothbot Voltaic": ["Tracking", "Precise", 0], "Air Angelic 4 Voltaic": ["Tracking", "Precise", 0],
        "PGTI Voltaic": ["Tracking", "Precise", 0], "FuglaaXYZ Voltaic": ["Tracking", "Reactive", 0],
        "Ground Plaza Voltaic": ["Tracking", "Reactive", 0], "Air Voltaic": ["Tracking", "Reactive", 0],
        "patTS Voltaic": ["Switching", "Speed", 0], "psalmTS Voltaic": ["Switching", "Speed", 0],
        "voxTS Voltaic": ["Switching", "Speed", 0], "kinTS Voltaic": ["Switching", "Evasive", 0],
        "B180T Voltaic": ["Switching", "Evasive", 0], "Smoothbot TS Voltaic": ["Switching", "Evasive", 0],
    }
}


def collect_data(easy: bool = True, benchmarks: dict = SCENARIOS) -> pd.DataFrame:
    bench = benchmarks["Easy"] if easy else benchmarks["Hard"]

    scenario_names = []
    accompaning_score = []
    dates = []
    scenario_type = []
    sub_type = []

    # if not path.isdir(folder): # if someone submitted nonsense
    folder = find_path() # try to get the path
    if type(folder) != str: # if that was not successful
        folder = "./" # populate with 0's
    for file_name in listdir(folder):
        name = file_name.split(" - Challenge")[0]
        if name in bench:
            # get the score
            with open(f"{folder}/{file_name}", "r") as f:
                score = search("Score:,(.*)\n", f.read()).group().strip().split(",")[-1]
            date = file_name.split()[-2].split("-")[0]
            if score.replace(".","",1).isdigit():
                scenario_names.append(name)
                accompaning_score.append(score)
                dates.append(date)
                scenario_type.append(bench[name][0])
                sub_type.append(bench[name][1])
                bench[name][-1] += 1

    for scenario in bench:
        if bench[scenario][-1] == 0:
            scenario_names.append(scenario)
            accompaning_score.append(0)
            dates.append("2021.9.15") # random day doesn"t really matter i just need placeholder value
            scenario_type.append(bench[scenario][0])
            sub_type.append(bench[scenario][1])

    return pd.DataFrame.from_dict({
        "scenario_name": scenario_names, "score": accompaning_score, 
        "date": dates, "scenario_type": scenario_type, "sub_type": sub_type,
    })


def find_path():
    bit_64 = "SOFTWARE\WOW6432Node\Valve\Steam"
    sub_dir = '/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats'
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hkey:
        with OpenKey(hkey, bit_64, 0, KEY_ALL_ACCESS) as sub_key:
            install_path = EnumValue(sub_key, 1)[1].replace("\\", "/")
    lib_path = install_path + "/steamapps/libraryfolders.vdf"
    potential_path = f'{install_path}{sub_dir}'
    if path.isdir(potential_path):
        return potential_path
    else:
        with open(lib_path, "r") as file:
            matches = findall('"path"		(.*)\n', file.read())
            matches = [i.replace("\\\\", "/").replace('"', "") for i in matches]
        for match in matches:
            if match != install_path:
                potential_path = f'{match}{sub_dir}'
                if path.isdir(potential_path):
                    return potential_path
    return -1


def clean_group(df: pd.DataFrame) -> pd.Grouper:
    # enforce types because there will be data manipulation and no more data collection
    df.score = df.score.astype("float")
    df.date = pd.to_datetime(df.date, format=r"%Y.%m.%d")

    groups = df.groupby("scenario_name")
    return groups


def main():
    return clean_group(collect_data(True)), clean_group(collect_data(False))
